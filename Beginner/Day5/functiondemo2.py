import datetime
from utilitiesmodule import *


def displayDetails(title, value, today = datetime.datetime.now()):
    banner(length=100, message=f'{title} | {today}')

    print(f"Length: {len(value)}")
    print(f"Value: {value}")


def displayDetails_v2(title, value, today = None):

    if(today is None):
        today = datetime.datetime.now()

    banner(length=100, message=f'{title} | {today}')

    print(f"Length: {len(value)}")
    print(f"Value: {value}")


def main():
    title = "Tuples Demo"
    tuplePerson = (1, 'Rajesh Agarwal', 24, 567.90)
    displayDetails(title, tuplePerson)

    tuplePerson = (2, 'Azim', 24, 567.90)
    displayDetails(title, tuplePerson)

    tuplePerson = (3, 'Mathews', 24, 567.90)
    displayDetails(title, tuplePerson)

    tuplePerson = (4, 'Rahul Iyer', 24, 567.90)
    displayDetails_v2(title, tuplePerson)

    tuplePerson = (5, 'Manish Sinha', 24, 567.90)
    displayDetails_v2(title, tuplePerson)

    tuplePerson = (6, 'Bhavya Singal', 24, 567.90)
    displayDetails_v2(title, tuplePerson)


main()
