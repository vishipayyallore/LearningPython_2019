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

def main():
    associate1 = Programmer('Mohd Hafeez', 21)
    print(associate1)

    associate2 = QA('Mathew Philips', 21)
    print(associate1)


    employee = Employee(associate1)
    employee.display_details()

    employee = Employee(associate2)
    employee.display_details()

main()
