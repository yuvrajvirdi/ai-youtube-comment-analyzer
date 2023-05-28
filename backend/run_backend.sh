#!/bin/bash

# create python virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bin/activate

# check if requirements.txt exists
if [ -f requirements.txt]; then
    echo "installing dependencies"
    pip install -r requirements.txt
    echo "installation done"
else:
    echo "requirements.txt not present"
    exit 1
fi

# run flask server
python main.py