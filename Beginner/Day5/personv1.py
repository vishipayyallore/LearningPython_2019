class Person:
    instances = 0

    def __init__(self, name = 'No Name'):
        Person.instances += 1

        self.name = name

    def display_details(self):
        print(f'Name: {self.name}')


def main():
    
    person3 = Person('Person Three')
    person3.display_details()

    person4 = Person()
    
    person1 = Person()
    print(person1.instances)
    print(f'Person 1: {person1.name}')

    person2 = Person('Azim')
    print(person1.instances, person2.instances)
    print(f'Person 2: {person2.name}')

    print('Are we same (instances): ', person1.instances is person2.instances)
    print('Are we same (name): ', person1.name is person2.name)
    print('Are we same (name): ', id(person1.name), id(person2.name))

main()