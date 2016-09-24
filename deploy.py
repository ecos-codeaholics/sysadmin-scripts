#!/usr/bin/python
# ...
# Andres Osorio - aosorio@uniandes.edu.co
# ...
import logging
import subprocess

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

steps = []

step0 = 'sudo -u ecos ./deploy_backend.py'

steps.append (step0)

steps_seq = ';'.join(steps)

exec_process( steps_seq )

