#!/bin/bash
# ...
# Jheison Rodriguez - jheison@uniandes.edu.co
# ...

#args=("$@")
#target=${args[0]}
#tag=${args[1]}

target="production"
tag="v3.0"

reponame="/factory-of-procedures-front"
frontend_repo="https://github.com/ecos-codeaholics/factory-of-procedures-front.git"
frontend_path="/home/"$USER"/typescript-apps/"$target
config_file="/home/"$USER"/typescript-apps/"production.json

setup_cmd="rm -rf "$frontend_path"/*"
getcode_cmd="git clone "$frontend_repo
settag_cmd="git checkout tags/"$tag
npminstall_cmd="/usr/bin/npm install"
frontconfig_cmd="cp -v "$config_file" ./src/config/"

# . execute commands
eval $setup_cmd
cd $frontend_path
eval $getcode_cmd
cd $frontend_path$reponame
eval $settag_cmd
eval $frontconfig_cmd
eval $npminstall_cmd
