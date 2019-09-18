Title: Introducing hypothesis-auto - An extension for Hypothesis that provides fully automatic testing for type hinted functions
Date: 2019-09-19 4:00
Author: timothycrosley
Category: New Project
Tags: Projects, 52, Introduction
slug: project-5-hypothesis-auto

[![hypothesis-auto Logo](https://raw.githubusercontent.com/timothycrosley/hypothesis-auto/master/art/logo_large.png)](https://timothycrosley.github.io/hypothesis-auto/)

| | |
| ------------| -----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| project: | 5/52 |
| Title/Link: | [hypothesis-auto](https://timothycrosley.github.io/hypothesis-auto/) |
| Pitch: | Have tests automatically generated for you. |
| Read if: | You are interested in increasing test coverage, utilizing property-based testing, or reducing the number of tests you need to write by hand. |
| Skip if: | You already heavily utilize Hypothesis or another property testing system. |
| Prior Work: | [Hypothesis](https://hypothesis.readthedocs.io/en/latest/), [QuickTest](http://hackage.haskell.org/package/QuickCheck). |

# Why Do We Even Write Tests?

Personally, my two biggest motivators for writing tests are to save time and to save face. Over and over again, I've experienced painless refactors and deploys where there are many useful tests,
and hours or days of toil picking up the pieces from when there are not. However, I've always felt something was missing from the tests I wrote.
They did a great job of keeping me from reencountering the same bugs! But, I would still often encounter what seemed later to be glaring issues in real-life usage.
The cases where there were many good test cases? Those test cases primarily came from issues users of my project had encountered.
As the number of regression tests grew, so did time before needing to add a new one. However, each regression test represented an error a user *already* encountered.
In attempts to reduce the number of bugs on the initial release of a project, I invested more and more into testing upfront.
Most projects I've released in the last few years were released with at or close to 100% test coverage. Still came the inevitable bug reports.

Of course, no matter how much we test, there will always be bugs in any sufficiently complex piece of software.
But, what can be done to reduce the number of genuinely embarrassing ones? Over time, my problem with TDD as the accepted solution to this problem has been
that it's too easy for me to fail in the same way twice. Writing the tests first assumes I'm going to pick the right test case to write
and then write the code in a way that matches the intentions of the test. It's certainly better than no testing. However, I often miss edge cases on either side of that equation. I often feel that my test cases are an attempt to outsmart myself in implementation. But, often it happens that I'm exactly as smart (or not) in similar ways when writing tests as I am implementing features.

# A Friend That Writes Test Cases

At work, I've often found a way to work around this problem is to ask coworkers what edge-cases concern them.
The difference in backgrounds and thought processes often leads to their edge-cases being very different from my own.
Once they've shared their edge cases, I then write up test cases that map to them. Sometimes they even write the test cases for me. I have great coworkers.
However, this isn't something I can rely on for my own small independent and often experimental projects. I need a friend that writes test cases for me.
But, I would never impose that on someone I considered a friend.

# Property-Based Testing

Clearly, I had to *build* such a friend. When researching this, I came across property-based testing, and it seemed like a perfect solution.
I then remembered a talk at PyCascades that went over the Python implementation of [Hypothesis](https://hypothesis.readthedocs.io/en/latest/),
and how it could, given a set of strategies, generate virtually infinite test cases for you. Who wouldn't want a friend like that? I was sold.
However, something felt a little off about using Hypothesis to me. In my newer code, I utilize mypy and type annotations to have well defined and typed public functions. But, when using Hypothesis, it felt like I often needed to repeat these typing definitions:

```python
from Hypothesis import given
import hypothesis.strategies as st


def add(number_1: int, number_2: int = 1) -> int:
    return number_1 + number_2


@given(st.integers(), st.integers())
def test_add(x, y):
    assert type(add(x)) == int
```

There must be a way to take it one step further and automatically generate test cases based on the type annotations?

# Introducing Hypothesis Auto

Rather than build a whole new property-based system from scratch, I decided to create an extension for Hypothesis. This extension would automatically generate test cases using the tested Callable's type annotations while allowing any parameters strategy to be replaced.
With hypothesis-auto, the above test becomes:

```python
from hypothesis_auto import from hypothesis_auto import auto_pytest_magic


def add(number_1: int, number_2: int = 1) -> int:
    return number_1 + number_2


auto_pytest_magic(add)
```

You can see this project [here](https://timothycrosley.github.io/hypothesis-auto/).

After building the extension, I immediately used it to improve [portray](https://timothycrosley.com/project-2-portray)'s test coverage and find/fix additional bugs in preparation for the 1.3.0 release of that project.
So far it's proving to be so easy to use against existing type hinted and pure functions, as to be a no-brainer addition to my test suites. Combined with [Examples](https://timothycrosley.github.io/examples/) to define and document the happy-path, static analysis, and a suite of regression tests as needed, I feel like I now have the tools I need to build code just robust enough not to be embarrassed.

# Thanks For Reading

Thanks for taking the time to read about this new project!
What do you think of hypothesis-auto? Any projects you would like to see in the future? Any projects I should try out?

~Timothy Crosley
