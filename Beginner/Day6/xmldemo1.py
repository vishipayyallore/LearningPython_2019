import xml.etree.ElementTree as etree
from pprint import pprint as pp
from utilitiesmodule import *

# filepath = './datastore/persons.xml'
filepath = './datastore/c2gen5_beta_t.xml'


xml_content = etree.parse(filepath)

control1 = xml_content.findall('GEN_CONFIG_TBL/FORMAT_CONTROL_1') 

char_format = xml_content.findall('GEN_CONFIG_TBL/FORMAT_CONTROL_1/CHAR_FORMAT')
print(f'Value: {char_format[0].text}')

banner("Pretty Print", 100)

print(type(xml_content))

for person in xml_content.findall('person'):
    print(type(person))
    
    print(person.find('firstName').text, end = ' | ')
    print(person.find('lastName').text, end = ' | ')
    print(person.find('age').text)
    
banner_v2(100)