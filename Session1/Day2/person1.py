"""
    This is my first program.
"""

def accept_and_display():
    roll_number = int(input('Enter Roll Number:'))
    first_name = input('Enter First Name:')
    last_name = input('Enter Last Name:')
    salary = float(input('Enter Salary:'))

    print('Person Details')
    print(f'Roll Number {roll_number}')
    print(f'Name {first_name} {last_name}')
    print(f'Salary {salary}')


accept_and_display()