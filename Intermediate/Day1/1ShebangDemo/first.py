#!/usr/bin/env python3
"""
    Program to demonstrate Basics of Input/Output
"""


# Importing Modules
import sys
import datetime

# Need to mention the path
sys.path.insert(0, '../2ModulesAndPyCache')
from utilitiesmodule import banner


class Person:

    # Calculating the date
    today = datetime.datetime.now().strftime('%c')

    def get_person_details(self):
        # Accepting Inputs from User
        self.name = input("Enter Your Name: ")
        self.employee_id = int(input("Enter Employee Id: "))
        self.salary = float(input("Enter Salary: "))
        self.is_manager = bool(int(input("Enter Manager Status {1 OR 0}: ")))

    def display_person_details(self):
        title = f"| Employee Details | Date: {self.today} |"

        # Displaying the output
        banner(title)
        print(f"\tName: {self.name}")
        print(f"\tId: {self.employee_id}")
        print(f"\tSalary: {self.salary}")
        print(f"\tIs Manager: {self.is_manager}")
        print("----------------------------------------------------")


def main():
    person = Person()
    person.get_person_details()
    person.display_person_details()


if __name__ == "__main__":
    main()
