import pickle


employees = {
    'A101': 'Shiva',
    'A102': 'Sai',
    'A103': 'Mathews',
    'A104': 'Philips',
}

filepath = './Data/employees.dat'

with open(filepath, 'wb') as empfile:
    pickle.dump(employees, empfile)
