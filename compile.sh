#!/bin/bash
set -e
git submodule update --recursive
pipenv run pelican-themes -U utterson
pipenv run pelican
