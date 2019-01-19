# ----------------------------------


class DataTypesDemo:
    Instances = 0

    def __init__(self, tupleObject):
        self.tupleObject = tupleObject
        DataTypesDemo.Instances += 1

    def displayDetails(self):
        print("----- DataTypesDemo Details -----")
        print('DataTypesDemo.Instances: ', self.Instances)
        print('Tuple Data: ', self.tupleObject)
        print()
# ----------------------------------


print("----- Tuples Demo -----")

# Defining a tuple without any element
tupleEmpty = ()
dataTypeObject = DataTypesDemo(tupleEmpty)
dataTypeObject.displayDetails()

#  Person Tuples
tuplePerson = (1, 'Shiva Sai', 24, 567.90)
dataTypeObject = DataTypesDemo(tuplePerson)
dataTypeObject.displayDetails()

#  Nested Tuples
tupleEmployee = (1, 'A1001', 24)
dataTypeObject = DataTypesDemo((tuplePerson, tupleEmployee))
dataTypeObject.displayDetails()

# Repetition Tuple
repeatTuple = ('Python 3',) * 4
dataTypeObject = DataTypesDemo(repeatTuple)
dataTypeObject.displayDetails()

# Slicing with tuples
sample_tuple = (0, 1, 2, 3, 4)

withoutFirstItem = sample_tuple[1:]
dataTypeObject = DataTypesDemo(withoutFirstItem)
dataTypeObject.displayDetails()

tupleReverse = sample_tuple[::-1]
dataTypeObject = DataTypesDemo(tupleReverse)
dataTypeObject.displayDetails()

from3to5Tuple = sample_tuple[2:5]
dataTypeObject = DataTypesDemo(from3to5Tuple)
dataTypeObject.displayDetails()
