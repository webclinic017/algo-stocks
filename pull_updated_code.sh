#!/bin/bash
#git submodule update --recursive --remote
#git pull --recurse-submodules
cd backtest
git checkout master
git pull
#
cd ../method
git checkout master
git pull
#
cd ../vn-stock-data
git checkout main
git pull
#
cd ..
git pull