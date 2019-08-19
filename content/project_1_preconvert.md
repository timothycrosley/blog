Title: Project  1/52: preconvert - Supercharge Your Serialization!
Date: 2019-08-18 23:00
Author: timothycrosley
Category: New Project
Tags: Projects, 52, Introduction
slug: project-1-preconvert

[![preconvert Logo](https://raw.githubusercontent.com/timothycrosley/preconvert/master/art/logo_large.png)](https://timothycrosley.github.io/preconvert/)

|             |                                                                                                                                                                        |
| ------------| -----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Project:    | 1/52                                                                                                                                                                   |
| Title/Link: | [preconvert](https://timothycrosley.github.io/preconvert/)                                                                                                             |
| Pitch:      | No more `is not JSON serializable` errors                                                                                                                              |
| Read if:    | You use JSON, MessagePack, BSON, or similar. Or, you are interested in the state of developing Python projects.                                                        |
| Skip if:    | You don't use serialization, only use it with basic built-in types, or only use it from the context of a framework that handles it well already.                       |
| Prior Work: | [https://hynek.me/articles/serialization/](https://hynek.me/articles/serialization/), [json-defaults](https://pypi.org/project/json-default/), and probably many more. |

# What Problem Does preconvert Solve?

My first project is a small one that comes the way of a goods friends request made at OSCON.
Many of us use Python's built-in `json` module or one of the similar serialization libraries available on PyPI.
These are trivially easy to use, and generally, work great. You pass in your native Python objects to `json.dumps` and your done:


```python
import json

json.dumps({"project": "preconvert"})
```

They even tend to follow the same loose specification (a `dumps` and corresponding `loads` method) making switching between them
for any reason equally straight forward.

```python
import simplejson as json

json.dumps({"project": "preconvert"})
```

This is pretty awesome! It's made even more so by the years of optimization these JSON libraries have received.
Not only is outputting JSON easy, but it's also fast.

Problems occur when you start going beyond the basic built-in types.
Search for `is not JSON serializable` and countless stack-overflow questions will appear with many workarounds for the problem.
The simplest of which is to override the `default` callback method provided by handling just the type that failed:

```python
import json
from uuid import UUID, uuid1


def fallback_conversion(item):
    if type(item) == UUID:
        return str(item)


json.dumps(uuid1(), default=fallback_conversion)
```

The above works great when you have one type you need to convert, and one place where you serialize data.
It works particularly badly if you are serializing data which you don't necessarily have full control of in multiple places.
Many web frameworks, including [hug](http://www.hug.rest/), provide mechanisms to get around this. They allow you to extend JSON serialization cleanly and provide built-in default serialization for most common types.

My friend, Brandon, suggested this shouldn't be hidden within the walls of a framework. Everywhere `json`, or another serializer is used, it should be trivial
to expand with custom types and handle common ones right out of the gate. I agreed, and preconvert was born.

# What's the Proposed Solution?

[preconvert](https://timothycrosley.github.io/preconvert/) is a small, framework independent, extendable Python library that aims to solve the above problems by:

1. Providing an easy way to specify custom type serializers

        import preconvert


        @preconvert.always(UUID)
        def convert_UUID_to_str(uuid_instance):
            return str(uuid_instance)

2. Using this ability to automatically handle common types (UUID, dataclasses, etc)
3. Adding an easy mechanism to extend this further using entrypoint powered plugins
4. Exposing the same interface defined by existing serializers to make preconvert an easy drop-in replacement.

        from preconvert.output import simplejson as json

preconvert currently works out-of-the-box with `bson`, `json`, `simplejson`, and `msgpack`.
Currently, there is one [plugin to handle numpy types](https://github.com/timothycrosley/preconvert_numpy), that can be enabled simply by adding it to the projects
package requirements.

    `pip install preconvert_numpy`

For more information about the project, browse the [documentation website](https://timothycrosley.github.io/preconvert/).

# State of Python Project Creation

One of the reasons I wanted to challenge myself to create 52 projects over this next year, was because I genuinely believe it shouldn't be hard to create projects.
While Python makes many things easy, it's surprising the number of things that should be considered for even a simple project.

## Documentation
For this project I used both [pdoc3](https://pdoc3.github.io/pdoc/) and [mkdocs](https://www.mkdocs.org/) for the first time.
[pdoc3](https://pdoc3.github.io/pdoc/) is probably the easiest route to document a Python project and I appreciated how it encouraged
me to write more expressive doc strings and better organize my project.
[mkdocs](https://www.mkdocs.org/) on the other hand has beautiful templates, integrates very well with the existing Markdown documentation I tend to include in GitHub repos,
and has built in search capabilities. However, mkdocs noticeably lacks any auto-documentation abilities at the current time.
To get around this, I created a build step that included customized [pdoc3](https://pdoc3.github.io/pdoc/) output that was compatible with what is expected by mkdocs.
I think it works fairly well, but I was disappointed with the lack of a robust all-in-one solution for simple projects.

## Local Environment Management
I gave [PipEnv](https://docs.pipenv.org/en/latest/) its first serious try. It worked alright, but I found it surprisingly slow.
It often was slow enough to make up for any time benefit it could have provided. I also found `pipenv run` and `pipenv shell` clunky to use.
Finally, I found it's lockfile to be confused when I switched machines constantly, my best guess is because of wheels for different platforms. Still, I'm glad to see project environment management become an increased area of focus.
For my next project, I intend to give [poetry](https://poetry.eustace.io/) a try.

## Packaging
I found [flit](https://github.com/takluyver/flit) to be an absolute joy to use. For the most part, it just worked and got out of my way.
It's simplified approach is perfect for small projects. The only downside I encountered, which unfortunately for me is a major one, is the lack of Cython support.

## Static Analysis
I'm a huge fan of static analysis, code formatters, and any tool that aims to raise the bar for code-quality on a project automatically.
This project included [all the ones I've used in the past](https://github.com/hugapi/HOPE/blob/master/all/HOPE-8--Style-Guide-for-Hug-Code.md#automated-code-cleaners), but also, [mypy](http://mypy-lang.org/). For the most part, it just worked.
As someone who is very comfortable with dynamically typed languages, I was surprised how little it impacted my productivity, and how even in this
small project it found real errors.

# Thanks For Reading

Thanks for taking the time to read about this new project!
What do you think of preconvert? Any projects you would like to see in the future? Any projects I should try out?

~Timothy Crosley
