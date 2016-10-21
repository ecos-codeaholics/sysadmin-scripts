#!/usr/bin/python
# ...
# Andres Osorio - aosorio@uniandes.edu.co
# ...
import logging
import os
import subprocess
import sys

logging.basicConfig(filename='deployback.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info('*')

def exec_process( cmd ):
	process  = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = process.communicate(cmd)
	return out, err

tag      = 'v1.1'
target   = 'production'
path     = 'java-apps'
src      = 'CA-Factory'
repo     = 'https://github.com/ecos-codeaholics/factory-of-procedures-back.git'
reponame = repo.split('/')[-1].split('.')[0]

location = path + '/' + target

steps = []

step0 = 'cd'
step1 = 'rm -rf ' + location + '/*'
step2 = 'cd ' + location
step3 = 'git clone ' + repo
step4 = 'cd ' + reponame + '/' + src
step5 = 'git checkout tags/' + tag
step6 = '/usr/local/maven/bin/mvn clean'
step7 = '/usr/local/maven/bin/mvn test'
step8 = 'git branch'
step9 = 'git tag'

# check first if directory exists

home = os.environ['HOME']

# now run the following steps

steps.append (step0)
steps.append (step1)
steps.append (step2)
steps.append (step3)
steps.append (step4)
steps.append (step5)
steps.append (step6)
steps.append (step7)
steps.append (step8)
steps.append (step9)

steps_seq = ';'.join(steps)

print steps_seq

#out,err = exec_process( steps_seq )
logging.info('deployment done')
