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
| Pitch: | Modern MIT fork of pdoc. Automatic Documentation from Code. |
| Read if: | You want to use pdoc but not AGPL OR are interested in documenting Python projects. |
| Skip if: | You don't create Python projects. Or, you've already created documentation sites for your Python projects and are happy with the tooling around them. |
| Prior Work: | [pdoc](https://github.com/mitmproxy/pdoc), [portray](https://timothycrosley.com/project-2-portray). |

# Sometimes We Don't Pick our Projects

You would think one of the great things about working on Open Source projects is that you can pick to work on whatever you want.
Your projects can reflect what you are most skilled in or passionate about. However, I discovered on my last project; this is not always the case.
If you want to be a good steward of an Open Source project you manage, you also have to be ready to handle issues with dependencies.

After releasing my last project, I was thrilled to see it hit the top of hackernews!
However, one thread brought up a controversy I noticed late into the project: [https://news.ycombinator.com/item?id=20803008](https://news.ycombinator.com/item?id=20803008).
But just as importantly, looking through the GitHub thread again made me aware an even bigger issue: pdoc3, unlike the original pdoc, is AGPL. All my projects, including portray, are licensed under MIT, which is not compatible with AGPL.

This led me to the realization I would need to fork the original pdoc and modernize it so it could handle the requirements set by portray.

# Creating pdocs

I decided to call my fork `pdocs` as I felt it had nice symmetry with the other portray dependency `mkdocs` while holding a dual meaning well:

1. Python Docs
2. pdoc successor

Most Open Source developers, my self included, don't look forward to forking an old project with a long history.
There's tends to be technical debt in old Open Source projects, just as there is in commercial ones. The moment you fork,
especially if your fork is successful, you own that debt. And, since you likely aren't the creator, you probably don't understand the debt you now possess.

`pdoc` was only partially an exception to this, as it turned out a ton of work had been done on the repository up until about a year ago, most of it being refactoring.
I still found a lot of dead code paths and was able to clean things up significantly, but at least the house was preparing to come to order.

`pdocs` includes the following improvements over `pdoc`:

1. Type hint support.
2. Simple programmatic API.
3. A ton of bug fixes.
4. Markdown generation support.

All of these were requirements for it to be able to replace `pdoc` usage within `portray.`

# Thanks For Reading

Thanks for taking the time to read about this new project!
What do you think of pdocs? Any projects you would like to see in the future? Any plans I should try out?

~Timothy Crosley
