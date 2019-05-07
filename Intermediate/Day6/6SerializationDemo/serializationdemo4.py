import pickle
from pprint import pprint as pp
from Employee import *

filepath = './Data/employee.dat'

with open(filepath, 'rb') as empfile:
    employee1 = pickle.load(empfile)

print(employee1)