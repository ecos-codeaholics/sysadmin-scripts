#!/usr/bin/python
# ...
# Andres Osorio - aosorio@uniandes.edu.co
# ...
import logging
import os

logging.basicConfig(filename='deployback.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info('*')

target   = 'development'
path     = 'java-apps'
src      = 'CA-Factory'
repo     = 'https://github.com/ecos-codeaholics/factory-of-procedures-back.git'
reponame = repo.split('/')[-1].split('.')[0]
branch   = '-b ' + target

location = path + '/' + target + '/' + reponame + '/' + src

steps = []

step0 = 'su ecos'
step1 = 'cd ' + location
step2 = 'git pull ' + repo
step3 = 'mvn clean'
step4 = 'mvn test'
step5 = 'git branch'
step6 = 'git tag'

# check first

if os.path.isdir(location):
	logging.info('local repo ready')
else:
	step1 = 'cd ' + path + '/' + target
	step2 = 'git clone ' + repo + ' ' + branch + ' ; cd ' + reponame + '/' + src
	logging.info('will clone repo')
	
steps.append (step1)
steps.append (step2)
steps.append (step3)
steps.append (step4)

steps_seq = ';'.join(steps)

results = os.popen(steps_seq,'r').readlines()
logging.info('deployment done')

final_steps = []
final_steps.append(step1)
final_steps.append(step5)
final_steps.append(step6)

steps_seq = ';'.join(final_steps)

results = os.popen(steps_seq,'r').readlines()
logging.info(results[0][:-1] + ' ' + results[1][:-1])





