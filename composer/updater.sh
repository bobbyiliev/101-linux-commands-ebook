#!/bin/bash

# To run this script, first cd to the composer directory.
# cd composer && . ./updater.sh

echo $(pwd);
cd .. && cd ./composer;
echo $(pwd);
python3 compose.py && \
    python3 nav_updater.py;
    echo $(pwd);
cd $TOP_LEVEL_DIR;
echo $(pwd);
