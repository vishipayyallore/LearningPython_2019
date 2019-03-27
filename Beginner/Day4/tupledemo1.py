from utilitiesmodule import *


def displayDetails(title, value):
    banner(length=100, message=title)

    print(f"Length: {len(value)}")
    print(f"Value: {value}")


title = "Tuples Demo"

# Defining a tuple without any element
tupleEmpty = ()
displayDetails(title, tupleEmpty)

#  Person Tuples
tuplePerson = (1, 'Shiva Sai', 24, 567.90)
displayDetails(title, tuplePerson)

#  Nested Tuples
tupleEmployee = (1, 'A1001', 24)
displayDetails(title, tuplePerson)

# Repetition Tuple
repeatTuple = ('Python 3',) * 4
displayDetails(title, repeatTuple)

# Slicing with tuples
title = 'Slicing with tuples'
sample_tuple = (0, 1, 2, 3, 4)

withoutFirstItem = sample_tuple[1:]
displayDetails(title, withoutFirstItem)

tupleReverse = sample_tuple[::-1]
displayDetails(title, tupleReverse)

from3to5Tuple = sample_tuple[2:5]
displayDetails(title, from3to5Tuple)
