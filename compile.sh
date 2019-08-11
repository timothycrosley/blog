#!/bin/bash
set -e
rm -rf utterson
git clone https://github.com/timothycrosley/utterson
pipenv run pelican-themes -U utterson
rm -rf utterson
pipenv run pelican
