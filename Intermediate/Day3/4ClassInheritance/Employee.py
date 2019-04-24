class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f'Name: {self.name} | Age: {self.age}')

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'


class Programmer(Employee):
    
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'

class QA(Employee):
    
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'


def main():
    associate1 = Programmer('Mohd Hafeez', 21)
    print(associate1)

    associate2 = QA('Mathew Philips', 21)
    print(associate2)


main()
