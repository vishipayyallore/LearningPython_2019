from pprint import pprint as pp

employees = {
    'A101': 'shiva',
    'A102': 'sai',
    'A103': 'mathews',
    'A104': 'philips',
}

for empid, empname in employees.items():
    print(empid, empname)

pp(employees)

employees_name_id = { empname.capitalize(): empid for empid, empname in employees.items()}
pp(employees_name_id)