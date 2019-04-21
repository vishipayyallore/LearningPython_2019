class Person:

    def display_details(self):
        print('I am Person::display_details()')


class PersonV1:

    def display_details(self, name):
        print(f'I am Person::display_details(). Hello {name}')


class PersonV2:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f'Name: {self.name}, Age: {self.age}')


class PersonV3:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f'Name: {self.name}, Age: {self.age}')

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'

    # Returns Dictionary
    def __repr__(self):
        return {'name':self.name, 'age':self.age}


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
        return self.__str__()

def main():
    person = Person()
    person.display_details()

    person1 = PersonV1()
    print('\nPerson 1 -----------')
    person1.display_details('Shiva Sai')

    person2 = PersonV2('Samuel Mathews', 21)
    print('\nPerson 2 -----------')
    person2.display_details()
    print(person2)
    print(str(person2))
    print(person2.__str__())
    print(person2.__repr__())

    person3 = PersonV3('Mohd Hafeez', 21)
    print('\nPerson 3 -----------')
    print(person3)
    print(person3)
    print(str(person3))
    print(person3.__str__())
    print(person3.__repr__())
    # print(repr(person3)) Throws Error

    person4 = PersonV4('No Name', 21)
    print('\nPerson 4 -----------')
    print(str(person4))
    print(person4.__str__())
    print(person4.__repr__())
    print(repr(person4)) 


if __name__ == "__main__":
    main()