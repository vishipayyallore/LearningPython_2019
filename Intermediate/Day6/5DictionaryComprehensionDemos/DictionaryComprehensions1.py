from pprint import pprint as pp

employees = {
    'A101': 'Shiva',
    'A102': 'Sai',
    'A103': 'Mathews',
    'A104': 'Philips',
}

for empid, empname in employees.items():
    print(empid, empname)

pp(employees)

employees_name_id = { empname: empid for empid, empname in employees.items()}
pp(employees_name_id)