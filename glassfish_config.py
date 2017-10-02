import xml.etree.ElementTree as ET

# Open original file
et = ET.parse('domain.xml')
root= et.getroot()
java_config = root.findall(".//java_config")

for child_1 in java_config:
    print(child_1.text)


jvm_options = root.findall(".//jvm-options")
print(jvm_options[0].text)
new_tag = ET.SubElement(et.getroot(), 'jvm-options')

new_tag.text = '-Djava.net.preferIPv4Stack=true'

jvm_options.append(new_tag)


# Write back to file
et.write('domain.xml')
#et.write('file_new.xml')