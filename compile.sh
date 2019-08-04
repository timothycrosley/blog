#!/bin/bash
set -e
git clone https://github.com/timothycrosley/attila.git
pelican-themes -i attila
rm -rf attila
pelican
