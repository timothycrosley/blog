Title: Introducing isort 5: The story of refactoring a widely used 10 year old project.
Date: 2020-08-09 4:30
Author: timothycrosley
Category: New Project
Tags: Projects, 52, Introduction
slug: project-8-isort5

[![isort 5 Logo](https://raw.githubusercontent.com/timothycrosley/isort/develop/art/logo_5.png)](https://timothycrosley.github.io/isort/)

| | |
| ------------| -----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| project: | 8/52 |
| Title/Link: | [isort](https://timothycrosley.github.io/isort/) |
| Pitch: | isort your imports, so you don't have to. |
| Read if: | You're interested in Python auto formatters or the challenges of refactoring widely used code that is a decade in the making. |
| Skip if: | You're not interested in auto formatters, or are only interested in brand new projects. |
| Prior Work: | [rope](https://pypi.org/project/rope/), [older versions of isort](https://www.reddit.com/r/Python/comments/1lr8gf/automatically_turn_messy_python_imports_into/) |

## Well, that took longer than expected.

I know. I know—52 projects in a year. A year has likely already passed, and I'm talking about project #8. I've learned a lot over the last year. I've switched jobs (hello Stripe!), celebrated my daughter's 1st birthday, and witnessed the world enter a pandemic. I have, however, NOT finished 52 projects. I knew it was unlikely I would reach the goal from the start, but I was sure either way, I would enjoy the journey, and I have! Hopefully, I've built some useful projects during that time as well. I indeed spent more of that improving one of my oldest projects than expected, but I'm glad I did. However, this put me at a cross-road. Keep the project goal, and give up the time goal. Or, keep the time limit and give up on the number of projects I wished to release. Or, I guess, just give up. I've decided to give up on the time limit. I've just had too much fun to stop now!

## The most downloaded auto-formatter for Python ever?

isort, for me, was a great lesson in how the Python community can take projects with very simple initial ambitions and grow them into useful and complete projects. When I created isort ten years ago, and then [released it online six years ago](https://www.reddit.com/r/Python/comments/1lr8gf/automatically_turn_messy_python_imports_into/), I envisioned it only as a tool for individual programmers to sort imports. Once. You know, to save a bit of time. Maybe with some editor integration for convenience. I thought I'd release it, get some suggestions for some alternative styles, and be done with it forever. Initially, it was so naive as to auto strip *all* comments to make this task easier (for isort not for the user). I mean, if you run it manually as a one-off command, you can always manually add back a couple of comments afterward as well?

The community, not me, had much grander ambitions. isort would be included in CI/CD pipelines. It would check every single change to every single Python file committed to master. If possible, it would automatically make those changes as well. And not just for small projects, for some of the largest Python codebases around. All of a sudden, taking such a naive approach as auto stripping all comments, no longer seemed like a good long term strategy. Over time, pull requests after pull request came in that fixed these kinds of problems. Eventually, isort was able to handle not only a large number of styles but also a large number of corner cases. Quickly, its test suite grew to be larger than its codebase. isort became useful. Not perfect. But good enough for many. As of this writing, isort has been downloaded 116 million times. Which AFAIK makes it the most downloaded auto-formatting tool for Python by at least 4x:

[![auto formatter downloads](images/isort_downloads.png)](https://pepy.tech/project/isort)

This doesn't mean as much as it might at first seem. After all, the other tools on this list encompass a much broader scope than just the formatting of imports. Part of it may be that isort's unique focus allows it to be used alongside any of these other formatters. Still reaching 100+ million downloads for my little import sorter, was something I never expected to see.

## The problem with isort's organic growth

Over a hundred people (180 as of this writing) have helped improve isort over the years. Fixing hundreds of bugs and introducing dozens of features. But what never changed, until isort 5, was the internal structure of isort. A structure that each fix and improvement, while pushing the project ahead, seemed to ingrain further.

From the beginning of isort, the core and bulk of functionality happened within the `__init__` method of a single class: `SortImports.` While always arguably a sub-optimal design decision, as a new Python programmer at the time, it didn't seem too bad when that core logic was only dozens of lines long. At the end of the isort 4.x series, that core logic had ballooned to hundreds of lines, with the containing class over a thousand lines long. Everything isort would do, internally, was accomplished by mutating attributes of that single class.

```
(input file) -> CLI interface -> SortImports(file, config, everything, as, class, init, **arguments) -> (output to same)
```

Another pain point was isort's initial design, only being centered around an individual developer running it on their machine.
As isort became a part of CI/CD systems, its initial trade-off to using as much magic as possible to determine what section an import belonged to, no longer fit the reality of how isort was run. This kind of magic led isort to work correctly on one machine while failing to categorize imports on another—a very frustrating experience when isort is acting as a gatekeeper for a codebase.

I'm still amazed by how far isort went with this approach. Eventually, however, I no longer even felt like I could take pride in the project I had created. Issues piled up that the current architecture couldn't solve. Corner case after corner case had been worked around, but these workarounds had been pegged onto the initial architecture. An architecture that was never planned.

## Refactoring the 10-year-old codebase

There were some initial attempts, from various brave souls, to refactor the isort code base, usually, around the usage of an AST. All of them failed. According to those who had tried, the major problem was that it was tough to keep all the existing configuration options, formats, etc. while also rebuilding the core from the ground up. So, when I finally decided I needed to clean up the code base, and solve the many issues that had been hanging over it, I decided to take a different tact.

To me, the biggest problem wasn't the lack of the usage of a traditional AST, that was actually a feature. isort didn't care about anything but imports. A traditional AST parsing approach would have isort parse an entire file, produce the Abstract Syntax Tree, identify the imports, mutate that tree as needed to sort them, and then output the tree into well-formatted code. Straight forward enough. But, that means isort would be parsing syntax it never cared about. Not only would this waste processor cycles and memory, but it would also unnecessarily make isort brittle, especially for editor based usage. One excellent advantage of isort from an integration perspective has always been that you can run it from any version of Python against any other. When things like the walrus operator came out, this broke many formatters, but isort would keep chugging along.

To me, the biggest problem with isorts internal structure was shared state and the associated lack of separation between concerns. You couldn't parse separately from formatting, and both actions freely mutated the same variables. This behavior resulted in tickets piling up, which desired things like sorting imports within functions, and no clear path for implementing them. So I started there. I would fully separate the parsing from the formatting, clearly defining the boundaries between both.

```
(input file) -> CLI interface -> parse.file_contents(file_contents) -> output.sorted_imports(parsed) -> (output file)

```

Much better! Immediately after finishing this separation, however, I noticed something else concerning. Parsing and output formatting both used the same config, which is fine. Maybe even expected. What wasn't anticipated was that both *mutated* this same config. This made it very hard to call them repeatedly with the same configuration, and just felt wrong. So, I decided to make the config creation happen first and separately, ensuring the configuration was immutable.

```
(input file) -> CLI interface -> ImmutableConfig(**options) -> parse.file_contents(file_contents, config) -> output.sorted_imports(parsed, config) -> (output file)
```

Finally, things that seemed out of reach before were easy. I was able to create a core function that simply identified groups of contiguous imports and parsed and then sorted them. I then put this new internal functionality behind dedicated Python APIs for common operations (such as formatting files and streams). Suddenly, I was able to work through the hundreds of issues open on isort's Github issue page at a steady pace. Still, while the initial refactor was relatively quick, finishing enough clean up that I felt proud of the project again took months. It was the first time in a while that I undertook a big project an open-source project, literally, one day at a time.

## Thanks For Reading

Thanks for taking the time to read about the making of isort 5!
What do you think of isort? Any projects you would like to see in the future? Any projects I should try out?

~Timothy Crosley
