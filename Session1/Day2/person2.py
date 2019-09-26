"""
    This is my first program.
"""

roll_number = 101
first_name = 'Mohd'
last_name = 'Hafeez'
salary = 1234.56

def accept_details():
    
    global roll_number, first_name, last_name, salary

    roll_number = int(input('Enter Roll Number:'))
    first_name = input('Enter First Name:')
    last_name = input('Enter Last Name:')
    salary = float(input('Enter Salary:'))

def dispaly_details():
    print('Person Details')
    print(f'Roll Number {roll_number}')
    print(f'Name {first_name} {last_name}')
    print(f'Salary {salary}')


# Invoking the methods
accept_details()
dispaly_details()
