from utilitiesmodule import *


def displayDetails(title, value):
    banner(length=100, message=title)

    print(f"Length: {len(value)}")
    print(f"Value: {value}")


title = "List Data Type Demo"


displayDetails('List Demo', [1, 2, 3])

# Empty List
listOne = []
displayDetails(title, listOne)

integerList = [10, 20, 30]
displayDetails(title, integerList)

squares = [1, 4, 9, 16, 25]
displayDetails(title, squares)

# Nested List
lowerCase = ['a', 'b', 'c', 'd']
upperCase = ['A', 'B', 'C', 'D']
numbers = [1, 2, 3, 4]
universalSet = [lowerCase, upperCase, numbers]
displayDetails("Nested List", universalSet)

print(universalSet[0][1])
print(universalSet[1][1])
print(universalSet[2][1])

for item in universalSet:
    print(item)
