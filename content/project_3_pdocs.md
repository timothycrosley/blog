Title: Introducing pdocs - Documentation Powered by Your Python Code
Date: 2019-09-03 4:00
Author: timothycrosley
Category: New Project
Tags: Projects, 52, Introduction
slug: project-3-pdocs

[![pdocs Logo](https://raw.githubusercontent.com/timothycrosley/pdocs/master/art/logo_large.png)](https://timothycrosley.github.io/pdocs/)

| | |
| ------------| -----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| project: | 3/52 |
| Title/Link: | [pdocs](https://timothycrosley.github.io/portray/) |
| Pitch: | Modern MIT fork of pdoc. Automatic Documentation from Python code. |
| Read if: | You want to use pdoc but not AGPL OR are interested in documenting Python projects. |
| Skip if: | You don't create Python projects. Or, you've already created documentation sites for your Python projects and are happy with the tooling around them. |
| Prior Work: | [pdoc](https://github.com/mitmproxy/pdoc), [portray](https://timothycrosley.com/project-2-portray). |

# Sometimes We Don't Pick our Projects

This next project isn't one I chose. I had many different ideas of what to work on after `portray,` but after that project unexpectedly [reached the top of hackernews](https://news.ycombinator.com/item?id=20800157), priorities changed.
I work on these projects with the hope that some of them will not only scratch an itch that I have but one that's shared with many other developers.
So I saw the interest shown in that post as a confirmation that I was on the right track. The most immediate fallout of this where improvements made to `portray` in the days following the post,
as can be seen in [portray's changelog](https://timothycrosley.github.io/portray/CHANGELOG/#changelog).
I was thrilled to be able to solve the most immediate pieces of user feedback quickly.

However, one thread brought up a controversy I noticed late into the project: [https://news.ycombinator.com/item?id=20803008](https://news.ycombinator.com/item?id=20803008).
I had hoped I could quickly pivot to using the original [pdoc](https://github.com/mitmproxy/pdoc) that pdoc3 was based on. If only to be able to bring the focus back to the problems I was trying to solve.
However, as I researched, I realized things wouldn't be quite so easy. [pdoc](https://github.com/mitmproxy/pdoc) hadn't seen a release since **2016**. It had, however, received code contribution up until
last year. Upon investigation, much of this work was broken, leading to the lack of a PyPI release. I was tempted to give up, but then I reread the GitHub conversation between the original pdoc maintainer
and the pdoc3 maintainer, and I knew I couldn't. When `pdoc` was forked into `pdoc3` the license was changed from ["Unlicensed"](https://unlicense.org/) to AGPL.
Because of the confusing naming and forking, when I had started working on portray, I saw the unlicense of pdoc and the MIT of mkdocs and missed the AGPL of pdoc3.
The license incompatibility of an MIT project using an AGPL project forced my hand. My next project would be a fork of the original pdoc.

# Creating pdocs

I decided to call my fork `pdocs` as I felt it had nice symmetry with the other portray dependency `mkdocs` while holding a dual meaning well:

1. Python Docs
2. pdoc successor

Now that I had a name decided, all I had to do was:

1. Fork the original project
2. Fix anything that might be wrong
3. Update portray to use the new fork
4. ???
5. Profit

Of course, it is much easier said than done. I have to guess that most Open Source developers don't look forward to forking an old project with a long history. I know I dreaded it.
There tends to be technical debt in old Open Source projects, just as there is in commercial ones. The moment you fork, especially if your fork is successful, you own that debt.
And, since you likely aren't the creator, you probably don't understand the debt you now possess.

The one thing I did have going for me, is that the work done on `pdoc` most recently was work to refactor it.
While the `pdoc` repository was in a broken disarray: the refactoring that had already been taken on made it much easier
to grasp:

- The logic was moved from a single module into many separate ones. Even better the boundaries where these modules were separated made sense (web, cli, doc, etc...)
- mypy typing was put in place
- Code auto-formatting and linting was put in place
- More tests were written

The CLI included numerous settings that didn't go anywhere and most simple commands I tried threw an exception, but the groundwork was in-place.

Over the next several days, I played whack-a-mole with various bugs as I encountered them.
Eventually, I took inventory of what I needed for portray, that pdoc even without bugs, didn't have:

- Type Annotation support
- Markdown output
- Python 3.6+ support

And one bonus:

- A straightforward API for portray to call

To accomplish this, I decided it would be best to split the API from the CLI as I did with `portray` while limiting the API and commands
to the bare minimum to start. I ended up with a stripped-down version of `pdoc` that could (given a list of modules):

- Serve documentation locally.
- Render documentation to HTML within a specified directory.
- Render documentation to Markdown within a specified directory.

And, that's it. Of course, it could do so both over HTTP and a simplified Python API.
By simplifying the scope, I was able to complete the first working fork in a reasonable amount of time, and quickly update `portray` to use it.
`pdocs` can't do everything `pdoc` could do, but it does everything `portray` used.
And, I hope, most of what users of `pdoc` use.

# Using pdocs from portray

Since I knew my intended use from the beginning, I tested pdocs against portray throughout the development.
So not only am I able to release pdocs today but also an updated portray that uses it.
If you currently use portray this change should be transparent to you unless you have manual pdoc3 settings defined.
If so, simply change your settings from living in `[tool.portray.pdoc3]` to `[tool.portray.pdocs]`

# Thanks For Reading

Thanks for taking the time to read about this new project!
What do you think of pdocs? Any projects you would like to see in the future? Any plans I should try out?

~Timothy Crosley
