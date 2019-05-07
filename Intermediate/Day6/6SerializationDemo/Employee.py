class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'


class Programmer(Employee):
    
    def __init__(self, name, age):
        super().__init__(name, age)


class QA(Employee):
    
    def __init__(self, name, age):
        super().__init__(name, age)
