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


def main():
    person = Person()
    person.display_details()

    person1 = PersonV1()
    person1.display_details('Azim')

    person2 = PersonV2('Mohd Hafeez', 21)
    person2.display_details()
    print(person2)

    person3 = PersonV3('Mohd Hafeez', 21)
    print(person3)


main()
