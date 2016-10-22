#!/bin/bash
# ...
# Jheison Rodriguez - jheison@uniandes.edu.co
# ...

target="development"

frontend_path="/home/"$USER"/GIT/Frontend/"$target"/factory-of-procedures-front" 
getcode_cmd="git pull"

cd $frontend_path
eval $getcode_cmd
