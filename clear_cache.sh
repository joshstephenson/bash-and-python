#!/usr/bin/env bash

find -E files -iregex ".+\.(txt|wav)" -exec rm -f {} \;
