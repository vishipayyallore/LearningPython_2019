"""This File is used for practice the programs daily
"""
class Employee:
    
    def __init__(self, associate):
        self.associate = associate

    def display_details(self):
        print(f'Name: {self.associate.name} | Age: {self.associate.age}')

    def __str__(self):
        return f'Name: {self.associate.name}, Age: {self.associate.age}'

class Programmer:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'


class QA:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'

a1 = Programmer('Shiva', 25)
print(a1)
e1 = Employee(a1)
e1.display_details()

a2 = QA('Manish', 25)
print(a2)
e1 = Employee(a2)
e1.display_details()