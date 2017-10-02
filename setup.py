import subprocess
import os
import xml.etree.ElementTree as ET

subprocess.call(['sudo', 'apt-get', 'update'])


#UTILS ETC ==========================================================================
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


# JAVA =================================================================================

subprocess.Popen( 'sudo apt-get install python-software-properties  debconf-utils -y',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()

subprocess.Popen( 'sudo add-apt-repository ppa:webupd8team/java -y',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()
subprocess.Popen( 'sudo apt-get update -y',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()
subprocess.Popen('echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | sudo debconf-set-selections', shell= True, stdin=subprocess.PIPE ).communicate()

subprocess.Popen( 'sudo apt-get install -y install oracle-java8-installer',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()

# AUTHBIND =================================================================================

subprocess.Popen( 'sudo apt-get install authbind -y',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()

subprocess.Popen( 'sudo touch /etc/authbind/byport/80',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()


subprocess.Popen( 'sudo touch /etc/authbind/byport/443',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()


subprocess.Popen( 'sudo chmod 500 /etc/authbind/byport/80',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()

subprocess.Popen( 'sudo chmod 500 /etc/authbind/byport/443',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()


subprocess.Popen( 'sudo chown glassfish /etc/authbind/byport/80',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()


subprocess.Popen( 'sudo chown glassfish /etc/authbind/byport/443',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()





# GLASSFISH =================================================================================

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

# GLASSFISH2 AUTHBIND =================================================================================


filesToConfig= ['/opt/payara41/glassfish/bin/asadmin','/opt/payara41/bin/asadmin','/opt/payara41/glassfish/lib/nadmin']

textToReplace = 'exec authbind --deep "$JAVA" -jar "$AS_INSTALL_LIB/client/appserver-cli.jar" "$@"'
textToSearch = 'exec "$JAVA" -jar "$AS_INSTALL_LIB/client/appserver-cli.jar" "$@"'


for file in filesToConfig:
    print(file)
    # Read in the file
    with open(file, 'r') as input_file :
      filedata = input_file.read()

    # Replace the target string
    filedata = filedata.replace( textToSearch, textToReplace)

    # Write the file out again
    with open(file, 'w') as out_file :
        out_file.write(filedata)


# GLASSFISH PASSWORDS ETC =================================================================================



subprocess.Popen( 'sudo chown -R glassfish:glassfish /opt/payara41/',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()



domain_file = '/opt/payara41/glassfish/domains/domain1/config/domain.xml'

et = ET.parse(domain_file)
root= et.getroot()
java_config = root.findall(".//java_config")

for child_1 in java_config:
    print(child_1.text)


jvm_options = root.findall(".//jvm-options")

new_tag = ET.SubElement(et.getroot(), 'jvm-options')

new_tag.text = '-Djava.net.preferIPv4Stack=true'

jvm_options.append(new_tag)

for child_2 in jvm_options:
    print(child_2.text)



# Write back to file
et.write(domain_file)

# GLASSFISH JACKSON FIX =================================================================================


subprocess.Popen( 'sudo wget --output-document=jackson-jaxrs-base.jar http://central.maven.org/maven2/com/fasterxml/jackson/jaxrs/jackson-jaxrs-base/2.8.4/jackson-jaxrs-base-2.8.4.jar',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()



subprocess.Popen( 'sudo wget --output-document=jackson-jaxrs-json-provider.jar http://central.maven.org/maven2/com/fasterxml/jackson/jaxrs/jackson-jaxrs-json-provider/2.8.4/jackson-jaxrs-json-provider-2.8.4.jar',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()


subprocess.Popen( 'sudo wget --output-document=jackson-databind.jar http://central.maven.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.8.4/jackson-databind-2.8.4.jar',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()

subprocess.Popen( 'sudo wget --output-document=jackson-core.jar http://central.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.8.4/jackson-core-2.8.4.jar',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()


subprocess.Popen( 'sudo wget --output-document=jackson-annotations.jar http://central.maven.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.8.4/jackson-annotations-2.8.4.jar',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()


subprocess.Popen( 'sudo wget --output-document=jackson-module-jaxb-annotations.jar http://central.maven.org/maven2/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.8.4/jackson-module-jaxb-annotations-2.8.4.jar',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate()

