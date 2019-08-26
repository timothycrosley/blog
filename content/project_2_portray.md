Title: Introducing portray - Your Project with Great Documentation
Date: 2019-08-26 4:00
Author: timothycrosley
Category: New Project
Tags: Projects, 52, Introduction
slug: project-2-portray

[![potray Logo](https://raw.githubusercontent.com/timothycrosley/portray/master/art/logo.png)](https://timothycrosley.github.io/portray/)

| | |
| ------------| -----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| project: | 2/52 |
| Title/Link: | [portray](https://timothycrosley.github.io/portray/) |
| Pitch: | Beautiful documentation websites for Python projects without the work. |
| Read if: | You create Python projects that could use browseable and searchable static documentation websites. |
| Skip if: | You don't create Python projects. Or, you've already created documentation sites for your Python projects and are happy with the tooling around them. |
| Prior Work: | [MkDoc](https://www.mkdocs.org/), [pdoc](https://pdoc3.github.io/pdoc/), [sphinx](http://www.sphinx-doc.org/en/master/). |

# A Birthday Gift to Myself

I decided to release `portray` today because today marks my 30th birthday. And, I couldn't think of a better gift to give myself then more and better documentation.
I know I'll use `portray` for the rest of the projects that I create, and retrofit my old ones to use it as well.
What would be even cooler is if even one developer creates a documentation website with portray when they wouldn't have created one otherwise.

# What Problem Does portray Solve?

In an ideal world, every programming project should have documentation. Python projects being no exception.
But, this documentation shouldn't come at the expense of writing elegant code and APIs.
Indeed, if things are working well, the two goals should complement each other.
One thing that often happens, though, is that documentation systems become complex.
This complexity can lead to accomplishing those two goals separately. And, when done independently it can be easy for them
to feel like they compete with each other.
One common way this dynamic plays out is in stale documentation. If code and documentation live too far from each other
but at a similar level of abstraction, this drift seems to be an inevitability.

This fact has lead to a sentiment that I have heard many times. And, indeed shared an appreciation for in the past. I'll summarize this sentiment as:

>   "Wrong documentation is worse than no documentation."

Which, of course, could be seen as conflicting with another common sentiment. The competing view is captured well on pdoc3's homepage:

>   "Documentation is like sex: when it is good, it is very, very good; and when it is bad, it is better than nothing."

In the [Zen of Hug](https://github.com/hugapi/HOPE/blob/master/all/HOPE-20--The-Zen-of-Hug.md) we summarize these seemingly competing desires as:

>   Wrong documentation is worse than no documentation.
>   Everything should be documented.

The reality, as is often the case, is that both sentiments have merit. In the end, almost everything we do as humans that is of significant complexity has errors.
If a documentation website helps solve the problems most users have while having a few incorrect sections, it is still a net good thing.
But, if a well-documented project is wrong in particularly critical sections - it might have been better with no documentation at all. In the end, the best thing to do may be to reduce the complexity as much as possible. And hope that by doing so, we reduce the separation of the goals and the corresponding errors.

One of the unfortunate things is that I believe these different viewpoints are reflected in the tools available. In general, at least in Python, we have two types of documentation systems:

- Automatic Reference Documentation:
 These systems include `pydoc`, `pdoc`, `pdoc3` and others. They take your existing code and docstrings and put it on a website.
 This can undoubtedly be useful. But, generally, this is the kind of documentation you look at as a reference once you are deep into a problem. Often, it feels it is easier to look at the code. This is especially true since these systems tend not to be searchable.
- Manual Documentation Systems:
 If the other systems view code as the first-class entity, these systems see documentation itself as the top priority.
 They need configuration files. They often suggest you put non-standard docstrings in your project. And, in general, they do everything they can to ensure that the outputted documentation is what is envisioned. These systems produce documentation websites that are searchable, browseable, configurable, and beautiful. Projects that support this line of thinking include: `sphinx` and to a lesser degree `MkDocs.`

In the end, what I've always wanted was a documentation generator that put both my code and the documentation I was generating on equal footing. I've wanted a documentation generator that was easy to use, searchable, and configurable only if I needed it to be. One that auto-generated reference docs, while enabling me to make beautiful quick start guides. I hope `portray` is that project.

# What's the Proposed Solution?

[portray](https://timothycrosley.github.io/portray/) is an automatic documentation website generator for Python projects. portray tries as much as possible to utilize existing work to accomplish the goals stated above. Under the hood, portray combines the Markdown documentation rendering capabilities provided by MkDocs with the automatic reference documentation generated by pdoc3.

I encourage you to look through the project's self-produced [documentation website](https://timothycrosley.github.io/portray/). I believe that website is the best overview I can give of `portray` as a documentation solution.

# Things I Experimented with When Making portray

Continuing from my last project, I wanted to explore a few new tools when making portray itself:

## Documentation
I used two new tools when making the documentation for `portray` itself.

- [asciinema](https://asciinema.org/) - Made it super easy to record CLI interaction. The only downside is the CLI sessions can't be placed directly on GitHub markdown pages. They can, however, be placed on `portray` produced documentation websites.
- [peek](https://github.com/phw/peek) - Made it trivially easy to record a section of my screen as a gif, which I used for the GitHub README.md file. I did, however, have to download an older version of the `.deb` due to [this issue](https://github.com/phw/peek/issues/434).

## Local Environment Management
For the last project, I gave [PipEnv](https://docs.pipenv.org/en/latest/) a run-through, for this one I used [poetry](https://Poetry.eustace.io/). From my experience, poetry wins hands down. It managed to replace flit, remove duplicate dependencies, and maintain stability across machines. All while using the standard `pyproject.toml` configuration file. Over time I'll be switching all my
projects to poetry. Sébastien, if you happen to read this, kudos your project is fantastic. That is all.

# Thanks For Reading

Thanks for taking the time to read about this new project!
What do you think of portray? Any projects you would like to see in the future? Any projects I should try out?

~Timothy Crosley
