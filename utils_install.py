import subprocess
import os

subprocess.Popen( 'sudo apt-get install unzip -y',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()


subprocess.Popen( 'sudo apt-get install ntpdate -y',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()
print("editing  /etc/cron.daily/ntpdate")
#edit ntupdate file
f = open('/etc/cron.daily/ntpdate', 'w')
f.write('#!/bin/sh \n /usr/sbin/ntpdate pool.ntp.org 1> /dev/null 2>&1')
f.close()

print("edited /etc/cron.daily/ntpdate")

subprocess.Popen( 'sudo chmod +x /etc/cron.daily/ntpdate',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()
subprocess.Popen( 'sudo /etc/cron.daily/ntpdate',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()

