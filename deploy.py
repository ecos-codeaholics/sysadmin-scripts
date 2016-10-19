#!/usr/bin/python
# ...
# Andres Osorio - aosorio@uniandes.edu.co
# ...
import logging
import subprocess

logging.basicConfig(filename='/var/log/deploy/deploy.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info('*')

under_supervision = ['back-factory-dev','front-factory-dev']

def exec_process( cmd ):
	process  = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	out, err = process.communicate(cmd)
	return out, err

def stop_supervisord(program):
	command  = 'supervisorctl stop ' + program
	out, err = exec_process( command )
	return out, err

def start_supervisord(program):
	command = 'supervisorctl start ' + program
	out, err = exec_process( command )
	return out, err

backend_script = '/home/ecos/sysadmin-scripts/' + 'deploy_backend.py'
frontend_script = '/home/ecos/sysadmin-scripts/' + 'deploy_frontend.py'

steps = []
step0 = 'sudo -u ecos ' + backend_script
step1 = 'sudo -u ecos ' + frontend_script

steps.append (step0)
steps.append (step1)
steps_seq = ';'.join(steps)

#1. stop under supervision programs
for pg in under_supervision:
	stop_supervisord(pg)

#2. execute deployment
out,err = exec_process( steps_seq )

#3. start under supervision programs
for pg in under_supervision:
	start_supervisord(pg)
