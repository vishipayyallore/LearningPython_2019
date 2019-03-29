import xml.etree.ElementTree as etree
from pprint import pprint as pp
from utilitiesmodule import *

filepath = './datastore/persons.xml'

xml_content = etree.parse(filepath)

banner("Pretty Print", 100)

print(type(xml_content))

for person in xml_content.findall('person'):
    print(type(person))
    
    print(person.find('firstName').text, end = ' | ')
    print(person.find('lastName').text, end = ' | ')
    print(person.find('age').text)
    
banner_v2(100)