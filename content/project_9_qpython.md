Title: Introducing QuickPYTHON: The fun of QBasic meets the power of Python
Date: 2020-11-26 10:00
Author: timothycrosley
Category: New Project
Tags: Projects, 52, Introduction
slug: project-9-qpython

[![QuickPYTHON Logo](https://raw.githubusercontent.com/timothycrosley/quickpython/master/art/logo_large.png)](https://timothycrosley.github.io/quickpython/)

| | |
| ------------| -----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| project: | 9/52 |
| Title/Link: | [QuickPYTHON](https://raw.githubusercontent.com/timothycrosley/quickpython/master/art/logo_large.png) |
| Pitch: | All the fun of QuickBASIC on old PCs but now using Python. |
| Read if: | You learned how to code on an old DOS computer using QuickBasic or TurboPascel, or if you are interested in unique coding environments.|
| Skip if: | You've already learned how to code, don't have any kids you want to teach, and aren't interested in unique coding environments. |
| Prior Work: | [QuickBasic](https://en.wikipedia.org/wiki/QBasic) [Turbo Pascal](https://en.wikipedia.org/wiki/Turbo_Pascal) [10 years later, QBasic is still the best](http://www.nicolasbize.com/blog/30-years-later-qbasic-is-still-the-best/) |
| Hackernews Article: | [Show HN: QuickPYTHON](https://news.ycombinator.com/item?id=25158588)

## One more minute, please! I'm almost done!

I'm a firm believer that addictions aren't *always* negative. When you find you're self addictive to positive things, some people might even mistake it for drive. Either way, those of you who have read my [whoami introduction](https://timothycrosley.com/whoami)
likely know that I became addicted to programming at a very young age. Since then, I've never been able to put it down. QuickBasic was my gateway drug. Any chance I got, I would spend hours making simple games, trying to automate
my homework, or building some crazy DOS UI. I didn't have access to the internet, but QuickBasic, with its built-in help, intuitive interaction with one button run, and simple mechanics, made it easy to pick up and hard to put down.

Learning to code these days feels different. In many ways, the environment in which I learned was defined by its limitations. I had two games on floppy disks. No internet and no money or means to buy more. If I wanted anything else, I had to make it myself. And the only way presented to do that was QBasic. Of course, the only way to learn it was to try things out and read the manual. That loop of trying new things, failing too many times, and then finally making something work is addictive in the best way possible. One of the biggest motivators to code was that the restricted content to consume created a huge contrast to the unlimited thing I was told I could make. Today, the content itself feels limitless. In the world I grew up in, given complete freedom, I naturally gravitated toward programming. I have to wonder if I had the same freedom as a kid these days if I would have just become addicted to Netflix and video games instead of programming.

My daughter isn't yet two and is unlikely to code anytime soon, but I've been thinking about whether it was even possible these days to introduce programming similarly in the back of my mind. Others have had the same thoughts and decided to [actually teach their kids to code using QuickBasic](http://www.nicolasbize.com/blog/30-years-later-qbasic-is-still-the-best/). I gave some thought but quickly had to admit how much some of QBasic's idioms, such as GOTO statements, set me back when I did graduate to more advanced programming languages. Python, I felt, would be a much better language to learn to code with initially. I spent some time to look and see if anyone had built anything as intuitive and straightforward as QBasic, but using Python - but I couldn't find anything. So, I decided to give a go at making such a programming environment myself, and QuickPython was born:

![Example Usage](https://raw.githubusercontent.com/timothycrosley/quickpython/master/art/example.gif)


## What is QuickPython

QuickPython is essentially a QBasic or TurboPascal like programming interface for Python. The idea is to fully contain everything you need to both learn how to code and run that code in a single place. No internet or external programs required. It's also just meant to be a fun project that brings back nostalgia feelings for anyone who learned to code on an old PC.

For the most part, QuickPython runs vanilla Python - though a few builtin extensions have been added for easier coding of terminal games:

- `cls()`: Clears the screen
- `beep()`: Makes a beep sound
- `@main`: Defines a method as the main method to start

It also comes with many example games written in Python that users can use as an inspiration to build their own, or just as one more local resource to learn the language.

Under the cover, QuickPython relies heavily on [Prompt Toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/) to power much of the UI features and is a single file almost exclusively edited with QuickPython.

## Thanks For Reading

Thanks for taking the time to read about this new project! What do you think of QuickPYTHON? Any projects you would like to see in the future? Any projects I should try out?

Happy Coding!

~Timothy Crosley
