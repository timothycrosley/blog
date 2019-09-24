Title: Introducing cruft - A tool to manage project boilerplate
Date: 2019-09-24 9:30
Author: timothycrosley
Category: New Project
Tags: Projects, 52, Introduction
slug: project-6-cruft

[![cruft Logo](https://raw.githubusercontent.com/timothycrosley/cruft/master/art/logo_large.png)](https://timothycrosley.github.io/cruft/)

| | |
| ------------| -----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| project: | 6/52 |
| Title/Link: | [cruft](https://timothycrosley.github.io/cruft/) |
| Pitch: | Create projects quickly from templates *and* keep them up to date against those same templates. |
| Read if: | You use Cookiecutter, or another project templating tool, and have struggled with managing the boilerplate they generate. |
| Skip if: | You don't create enough individual projects to gain value from a project templating system. |
| Prior Work: | [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/), [Quickly](https://www.youtube.com/watch?v=9EctXzH2dss), [instantly](https://github.com/timothycrosley/instantly) |

# What's Wrong with Cookiecutter?

I have to start by saying, I *love* [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/). It allows creating standardized project definitions and then makes those standardized definitions the least friction way to create a new project.
This is a beautiful thing. And not just because it saves time. The ease of Cookiecutter templates has often led to them becoming a central place to define how a kind of project *should* be structured.
As a result, popular template repositories receive many pull requests, issues, and improvements over time. What's not to love? Lot's of things. I should mention, I also *hate* Cookiecutter. In my personal experience, the use of Cookiecutter has directly contributed to hard to maintain graphs of copy-and-pasted code.

# We've Automated Copying and Pasting

Copying and Pasting code as a process is terrible. Most engineers I've talked to agree with this. However, with tools like Cookiecutter, copying-and-pasting code has become so efficient that it can be easy to forget.
Worse, it is even easier to do so blindly, because you just run the command and the code appears. Why is it so bad? Your project lives after project creation.  Each line of code has costs, copy and pasted or not. Over time you start to feel those costs. Even a simple change, like [removing a deprecated config option](https://github.com/timothycrosley/cookiecutter-python/commit/8a65a360d51250221193ed0ec5ed292e72b32b0b),
can have rippling changes as you have to update every project by hand to include the improvement. Worse, because Cookiecutter makes it easy to add a lot of structure, smart engineers often get seduced
into using hard to maintain non-DRY solutions. Have a bunch of queue processing projects that all get built the *exact* same way that is represented by a hundred or more line Makefile? Without Cookiecutter
many engineers would do *something* to automate that and share steps between projects. With Cookiecutter, the cost of that large build file is deferred. So, many will just push the duplicate code approach and then be surprised when down the
road they have to make the same changes to all their projects. What is this, but starting a project with a significant continued source of technical debt? And this, in the end, is what much of Cookiecutter output
represents, technical debt. Often, it's technical debt from ecosystems the end-user doesn't control (such as unwieldy and large setup files). Cookiecutter lets you ignore that the upstream system has poor abstractions when you create the project, but those poor abstractions still exist. Sadly, tools like Cookiecutter end up celebrating the automation of project creation but rarely
highlight to the user the cost associated with this automation.

# Introducing cruft
To help solve the maintenance problem associated with project templates, I've created a tool called [cruft](https://timothycrosley.github.io/cruft/). It's called cruft for the same reason Chrome is called Chrome:
It's an acknowledgment, to both the end-user and the project, that project templates can quickly become sources of cruft and expanding boilerplate in projects. cruft believes this boilerplate, while often
necessary, is something to be managed not something to be celebrated. cruft uses Cookiecutter behind the scenes to expand templates, making it fully compatible with existing templates, but it does so in a more maintainable way.
So how does cruft help solve this problem? When you create a project with cruft, it adds a single additional file to your project `.cruft.json`:

```json
        {
            "template": "https://github.com/timothycrosley/cookiecutter-python",
            "commit": "8a65a360d51250221193ed0ec5ed292e72b32b0b",
            "context": {
                "cookiecutter": {
                    "full_name": "Timothy Crosley",
                    "email": "timothy.crosley@gmail.com",
                    "github_username": "timothycrosley",
                    "project_name": "cruft",
                    "description": "Allows you to maintain all the necessary cruft for packaging and building projects separate from the code you intentionally write. Built on-top of CookieCutter.",
                    "version": "0.0.1",
                    "_template": "https://github.com/timothycrosley/cookiecutter-python"
                }
            }
        }
```

This file contains the template you used to create your project, the git commit hash at time of creation, and every parameter that was passed to Cookiecutter.
cruft is then able to utilize this to help you keep your project in sync with the parent template.

- `cruft check` will return an error if the template has received updates that the project hasn't been updated to include. Perfect for inclusion in a CI/CD pipeline.
- `cruft update` will present the changes introduced by the template and ask if you want to apply them.

These simple additions allow you to keep your projects in-sync with the template they came from overtime. Even better, they make these changes visible to you, so you see the costs associated
with large and unwieldy templates, and are encouraged to templatize only the subset of code that makes sense.

Find out more about cruft on its website: [here](https://timothycrosley.github.io/cruft/)

# Thanks For Reading

Thanks for taking the time to read about this new project!
What do you think of cruft? Any projects you would like to see in the future? Any projects I should try out?

~Timothy Crosley
