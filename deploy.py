#!/usr/bin/python
# ...
# Andres Osorio - aosorio@uniandes.edu.co
# ...
import logging
import subprocess
import os

logging.basicConfig(filename='/var/log/deploy/deploy.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info('*')

def exec_process( cmd ):
	process  = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	out, err = process.communicate(cmd)
	return out, err

def stop_supervisord():
	command  = 'supervisorctl stop back-factory-test'
	out, err = exec_process( command )
	return out, err

def start_supervisord():
	command = 'supervisorctl start back-factory-test'
	out, err = exec_process( command )
	return out, err

home = os.environ['HOME']

backend_script = home + '/sysadmin-scripts/' + 'deploy_backend.py'

steps = []
step0 = 'sudo -u ecos ' + backend_script
steps.append (step0)
steps_seq = ';'.join(steps)

#1. stop supervisor 
stop_supervisord()

#2. execute deployment
exec_process( steps_seq )

#3. start supervisor
start_supervisord()
