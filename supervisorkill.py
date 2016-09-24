#!/usr/bin/python
# ...
# Andres Osorio - aosorio@uniandes.edu.co
# ...

import os,sys
import signal

psCmd = "ps -ef | grep supervisord"
kill = "kill "
sig = signal.SIGTERM
results = os.popen(psCmd,'r').readlines()
success = False

for rs in results:
    psresult = rs[:-1]
    if psresult.find("/bin/supervisord") > 1:
       pid = int(psresult.split()[1])
       os.killpg(pid, sig)
       #killCmd = kill + pid
       #os.system(killCmd)
       success = True

if success == True:
    print "supervisord killed .... [OK]"
else:
    print "supervidord not found running .... [0]"

