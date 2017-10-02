import subprocess
import os






os.chdir('/opt/')

subprocess.Popen( 'sudo wget https://s3-eu-west-1.amazonaws.com/payara.co/Payara+Downloads/Payara+4.1.1.163/payara-4.1.1.163.zip',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()

subprocess.Popen( 'sudo unzip payara-4.1.1.163.zip',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()



subprocess.Popen( 'sudo chmod 775 /opt/payara41/glassfish/bin/asadmin',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()



subprocess.Popen( 'sudo chmod 775 /opt/payara41/bin/asadmin',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()



subprocess.Popen( 'sudo chmod 775 /opt/payara41/glassfish/lib/nadmin',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()

