"""This File is used for practice the programs daily
"""

class PersonV4:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f'Name: {self.name}, Age: {self.age}')

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'

    # Returns String Representation
    def __repr__(self):
        # return {'name': self.name, 'age': self.age}
         return self.__str__()


person = PersonV4(age=21, name='Mathews')
person.display_details()
print(person)
print(person.__str__())
print(person.__repr__())
print(repr(person))
