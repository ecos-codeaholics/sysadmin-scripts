#!/usr/bin/python
# ...
# Andres Osorio - aosorio@uniandes.edu.co
# ...
import logging
import os
import subprocess
import sys

logging.basicConfig(filename='/var/log/deploy/deployback.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info('*')

def exec_process( cmd ):
	process  = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = process.communicate(cmd)
	return out, err

target   = 'development'
path     = 'java-apps'
src      = 'CA-Factory'
repo     = 'https://github.com/ecos-codeaholics/factory-of-procedures-back.git'
reponame = repo.split('/')[-1].split('.')[0]
branch   = '-b ' + target

location = path + '/' + target + '/' + reponame + '/' + src

steps = []

step0 = 'cd'
step1 = 'cd ' + location
step2 = 'git pull ' + repo
step3 = '/usr/local/maven/bin/mvn clean'
step4 = '/usr/local/maven/bin/mvn test'
step5 = 'git branch'
step6 = 'git tag'

# check first if directory exists

home = os.environ['HOME']

if os.path.isdir(home + '/' + location):
	logging.info('local repo ready')
else:
	step1 = 'cd ' + path + '/' + target
	step2 = 'git clone ' + repo + ' ' + branch + ' ; cd ' + reponame + '/' + src
	logging.info('will clone repo')

# now run the following steps

steps.append (step0)
steps.append (step1)
steps.append (step2)
steps.append (step3)
steps.append (step4)

steps_seq = ';'.join(steps)

print steps_seq

out,err = exec_process( steps_seq )
logging.info('deployment done')

# and finalise with these steps

final_steps = []
final_steps.append(step5)
final_steps.append(step6)

steps_seq = ';'.join(final_steps)

out,err = exec_process( steps_seq )
logging.info('verify:')
