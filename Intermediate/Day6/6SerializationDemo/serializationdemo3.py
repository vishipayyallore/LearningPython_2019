import pickle
from pprint import pprint as pp
from Employee import *

filepath = './Data/employee.dat'

employee1 = Programmer('Shiva Sai', 18)

with open(filepath, 'wb') as empfile:
    pickle.dump(employee1, empfile)

