Title: Introducing eXamples - Python Tests and Documentation Done by Example
Date: 2019-09-11 3:00
Author: timothycrosley
Category: New Project
Tags: Projects, 52, Introduction
slug: project-4-examples

[![examples Logo](https://raw.githubusercontent.com/timothycrosley/examples/master/art/logo_large.png)](https://timothycrosley.github.io/examples/)

| | |
| ------------| -----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| project: | 4/52 |
| Title/Link: | [eXamples](https://timothycrosley.github.io/examples/) |
| Pitch: | Examples that double as tests and documentation while enabling interactive discovery. |
| Read if: | You want your project to have more examples, tests, and documentation, but you have limited time to invest in all of them. |
| Skip if: | You are happy with doctest or have the resources to dedicate fully to each area, and discipline to keep them in sync. |
| Prior Work: | [doctest](https://docs.python.org/3/library/doctest.html), [hug](https://github.com/hugapi/hug). |

# You May Never be Able to Find this Project Again

... Or you may run into it way too often. I'm not sure what the result of using such a ubiquitous programming term such as "examples"  as the project name will have. I suppose we are about to find out.
When I saw the name was available on PyPI, I couldn't resist using a name that perfectly reflected what the project did.
Luckily, Python3 did away with implicit relative imports, or such a name would likely cause all sorts of local conflicts for those who installed it.
Just in case I've also registered the project under the much more unique name "xamples".

# What Problem Does eXamples Solve?

When creating, or maintaining a project with a public API, examples are a must to demonstrate to new users (or yourself a few months down the line) everyday use cases against your API.
A lot of time, a single usable example that a user can interact with, can answer the same question that may require pages of documentation to understand.
However, where to put function level examples has never felt evident to me. You can try your best to keep them in-sync in a docstring. Maybe even using something like doctest,
that interacts with your docstring like it is code. Or, you can place your examples in test cases and hope that users know to look there. Of course, at the time of using an API, they may not
even have your tests easily accessible. And what if some of the APIs end up exposed over an HTTP service? How could you define your examples so they can be utilized
to provide examples to API users over those mediums?

# What's the Proposed Solution?

[eXamples](https://timothycrosley.github.io/examples/) tries to answer these question for examples, in the same way, that type annotations answer it for parameter types. By moving the examples into programmatic
definitions associated with the functions on which they operate, instead of within unassociated code, or worse, a free-text field (the `__doc__` string).
Once done, it becomes trivial to reuse examples for multiple purposes. The eXamples library enables quickly creating these examples, verifying them against the function signature, and utilizing them as
test cases. And, of course, it makes them programmatically available. This means, that over time, projects like [hug](github.com/timothycrosley/hug) can automatically detect examples
you have on API endpoint functions. It can then provide them to users of your HTTP or Command Line interfaces. Finally, eXamples, by default, adds your examples to your docstring, in a way that renders beautifully on
[portray](https://timothycrosley.github.io/portray/) and [pdocs](https://timothycrosley.github.io/pdocs/).

Creating examples using eXamples is as easy as adding an example decorator per example with parameters that match the definition of the attached function:

```python3
from examples import example


@example(1, 1)
def sum(number_1: int, number_2: int) -> int:
    return number_1 + number_2
```

For a full overview of how this works and what it enables, see the projects [documentation website](https://timothycrosley.github.io/examples/).

# Things I Experimented with When Making eXamples

Since, unlike pdocs, this was a greenfield project, I had some flexibility to try out some new things when building it.

## pydantic

I looked into a variety of approaches to verify the type signatures of provided examples matched that expected.
I had hoped, I could find a way to call mypy programmatically on a single function. But, it proved, if nothing else, not to be an intended use case.
After looking through several runtime type validation libraries, many now defunct, I decided to use the one I've seen most commonly: [pydantic](https://pydantic-docs.helpmanual.io/).
In testing so far, it seems to work reasonably well. The only unfortunate thing is that it seems to want to validate class schemas only, instead of arbitrary functions
that have type hints. I was able to work around this by dynamically creating the schema class [using pydantics create_model utility function](https://github.com/timothycrosley/examples/blob/master/examples/example_objects.py#L50) against the information garnered by introspecting
the provided function.

## functools.singledispatch

I wanted to enable eXample's core API functions to be callable from multiple scopes (function, module, global). This seemed like an excellent opportunity to utilize [singleddispatch](https://www.python.org/dev/peps/pep-0443/) for the first time.
Overall, it was intuitive and seemed like an excellent way to provide structure around what would otherwise be done in a series of if-else statements.
I did get tripped up by the fact that it doesn't allow that single argument to be optional. But, after reflecting, I felt the decorator's limitations were helping to guide me into a better more consistent
API design.

# Thanks For Reading

Thanks for taking the time to read about this new project!
What do you think of eXamples? Any projects you would like to see in the future? Any projects I should try out?

~Timothy Crosley
