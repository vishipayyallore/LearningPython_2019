def get_person_details():
    return 101, "Shiva Sai", True, 1234.56


def display_person_details(person):
    print(f'Employee Id: {person[0]}')
    print(f'Name: {person[1]}')    
    print(f'Is Manager: {person[2]}')
    print(f'Salary: {person[3]}')