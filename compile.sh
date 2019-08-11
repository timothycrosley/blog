#!/bin/bash
set -e
#git clone git clone git@github.com:mamcmanus/brutalistpelican.git
#pelican-themes -i brutalistpelican
#rm -rf brutalistpelican
rm -rf utterson
git clone https://github.com/timothycrosley/utterson
pelican-themes -U utterson
rm -rf utterson
pelican
