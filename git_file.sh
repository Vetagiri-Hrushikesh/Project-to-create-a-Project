#!/bin/bash

function git_creation(){
    # cd  # To run the command from any directory.
    cd /Users/mac/Desktop/PROJECTS/PYTHON_AUTOMATION/AUTOMATIC_PROJECT/ROUGH\ KNOWLEDGE
    python git_creation.py $1
    cd /Users/mac/Desktop/Testing/$1
    git init
    git remote add origin https://github.com/Vetagiri-Hrushikesh/$1.git
    touch sample.txt
    git add .
    git commit -m "Initial Commit"
    git push -u origin master
    code .
}