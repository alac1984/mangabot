#!/bin/bash

# Full path to the python script
main_path="./main.py"

# Check if the script exists
if [ ! -f $main_path ]; then
    echo "Error: File $main_path does not exist."
    exit 1
fi

# Run the python script
python3 $main_path
