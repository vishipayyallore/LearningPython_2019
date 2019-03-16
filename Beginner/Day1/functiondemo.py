"""
    Program to demonstrate Basics of Input/Output
"""

# Importing Modules
import datetime


# Variables with Global Scope
name = ''
employee_id = 0
salary = 0.0
is_manager = False


'''
    Method to accept into for Employee
'''
def get_employee_details():
    
    # making the variables global, so that we can use into another function
    global name, employee_id, salary, is_manager

    # Accepting Inputs from User
    name = input("Enter Your Name: ")
    employee_id = int(input("Enter Employee Id: "))
    salary = float(input("Enter Salary: "))
    is_manager = bool(input("Enter Manager Status: "))


"""
    Method to display the Employee Details
"""
def show_employee_details():
    # Calculating the date
    todays_date = datetime.datetime.now()
    today = todays_date.strftime('%c')

    # Displaying the output
    print("====================================================")
    print(f"Employee Details | Date: {today} |")
    print("====================================================")
    print(f"\tName: {name}")
    print(f"\tId: {employee_id}")
    print(f"\tSalary: {salary}")
    print(f"\tIs Manager: {is_manager}")
    print("----------------------------------------------------")


"""
    main method will invoke other method.
"""
def main():
    get_employee_details()
    show_employee_details()


# Starting the program
main()
