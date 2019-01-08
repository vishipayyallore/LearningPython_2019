print("----- Tuples Demo -----")

class DataTypesDemo:
    Instances = 0

    def __init__(self, tupleObject ):
        self.tupleObject = tupleObject
        DataTypesDemo.Instances += 1

    def displayDetails( self ):
        print("----- DataTypesDemo Details -----")
        print('DataTypesDemo.Instances: ', self.Instances)
        print('Tuple Data: ', self.tupleObject)
        print()

# Defining a tuple without any element
tupleEmpty = ()
dataTypeObject = DataTypesDemo(tupleEmpty)
dataTypeObject.displayDetails()

tuplePerson = (1, 'Shiva Sai', 24,567.90)
dataTypeObject = DataTypesDemo(tuplePerson)
dataTypeObject.displayDetails()

# TODO: Work on nested Tuples
tupleEmployee = (1, 'A1001', 24)
dataTypeObject = DataTypesDemo( (tuplePerson, tupleEmployee) )
dataTypeObject.displayDetails()

