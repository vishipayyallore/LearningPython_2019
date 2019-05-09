import pickle
from pprint import pprint as pp

filepath = './Data/employees.dat'

with open(filepath, 'rb') as empfile:
    employees = pickle.load(empfile)


pp(employees)

for id, name in employees.items():
    print(id, name)

    