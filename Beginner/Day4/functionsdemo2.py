

def modify_values(id, name, subjects):
    id = 102
    name = 'Rajesh Agarwal'
    subjects[0] = -101

    print(f'(Inside modify_values) Id= {id}, Name= {name}, Subjects= {subjects}')

def modify_values_v2(id, name, subjects):
    id = 102
    name = 'Rajesh Agarwal'
    subjects[0] = -101

    print(f'(Inside modify_values) Id= {id}, Name= {name}, Subjects= {subjects}')

id = 100
name = 'Mohd Hafeez'
subjects = [1, 2, 3, 4]
print(f'(Outside modify_values) Id= {id}, Name= {name}, Subjects= {subjects}')

modify_values(id, name, subjects)

print(f'(Outside modify_values) Id= {id}, Name= {name}, Subjects= {subjects}')


subjects = [1, 2, 3, 4]
modify_values_v2(id, name, subjects[:]) # Sending a copy

print(f'(Outside modify_values) Id= {id}, Name= {name}, Subjects= {subjects}')

