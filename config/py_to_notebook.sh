#!/bin/bash

dir_this_file="$( dirname "$0" )"
dir_this_repo="$dir_this_file/.."

find "$dir_this_repo" -path '*/notebook/*.py' | xargs -I '{}' echo python "$dir_this_file/py_to_notebook_v4.py" --overwrite -f '{}'
