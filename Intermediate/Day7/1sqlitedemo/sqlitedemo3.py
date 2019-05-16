import sqlite3

connection = sqlite3.connect('./data/newemployees.db')

c = connection.cursor()

# get the count of tables with the name
c.execute(
    '''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='employees';''')

create_table = '''CREATE TABLE employees (ID INT PRIMARY KEY     NOT NULL, NAME TEXT NOT NULL);'''

# if the count is 1, then table exists
if c.fetchone()[0] == 0:
    print('Table does not exists.')
    connection.execute(create_table, )


id = int(input('Enter Id: '))
name = input('Name: ')
insert_data = f'INSERT INTO employees values ({id}, \'{name}\');'
connection.execute(insert_data);

id = int(input('Enter Id: '))
name = input('Name: ')
insert_data = f'INSERT INTO employees values ({id}, \'{name}\');'
connection.execute(insert_data);

select_data = '''SELECT * FROM employees;'''
datasets = connection.execute(select_data);

for id, name in datasets:
    print(id, name)

connection.commit()
connection.close()

print("Data Saved into Database Successfully");

