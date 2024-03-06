#!/bin/bash
if command -v python3 &>/dev/null; then
    echo "Python 3 is installed"
else
    echo "Python 3 is not installed"
    sudo apt-get install python3
fi

if command -v pip3 &>/dev/null; then
    echo "pip3 is installed"
else
    echo "pip3 is not installed"
    sudo apt-get install python3-pip
fi

python3 -m venv venv && source ./venv/bin/activate && pip3 install -r requirements.txt