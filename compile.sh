#!/bin/bash
set -e 
rm -rf venv
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
git clone https://github.com/timothycrosley/attila.git
pelican-themes -i attila
rm -rf attila
pelican
