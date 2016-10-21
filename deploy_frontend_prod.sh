#!/bin/bash
# ...
# Jheison Rodriguez - jheison@uniandes.edu.co
# ...

#args=("$@")
#target=${args[0]}
#tag=${args[1]}

target="production"
tag="v2.0"

reponame="/factory-of-procedures-front"
frontend_repo="https://github.com/ecos-codeaholics/factory-of-procedures-front.git"
frontend_path="/home/"$USER"/typescript-apps/"$target

setup_cmd="rm -rf "$frontend_path"/*"
getcode_cmd="git clone "$frontend_repo
settag_cmd="git checkout tags/"$tag

# . execute commands
eval $setup_cmd
cd $frontend_path
eval $getcode_cmd
cd $frontend_path$reponame
eval $settag_cmd
