"""To verify the return type of function
"""

roll_number = 101
first_name = 'Mohd'
last_name = 'Hafeez'
salary = 1234.56

def dispaly_details():
    print('Person Details')
    print(f'Roll Number {roll_number}')
    print(f'Name {first_name} {last_name}')
    print(f'Salary {salary}')


def dispaly_details_v1():
    print('Person Details')
    print(f'Roll Number {roll_number}')
    print(f'Name {first_name} {last_name}')
    print(f'Salary {salary}')

    return # Explicit Return

return_value = dispaly_details()
print(f'Value : {return_value}')

return_value = dispaly_details_v1()
print(f'Value : {return_value}')
