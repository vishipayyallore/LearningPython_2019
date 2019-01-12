class StringDataTypeDemo:
    Instances = 0

    def __init__( self ):
        StringDataTypeDemo.Instances += 1

    def displayDetails( self, title, value ):
        print(f"----- {title} -----")
        print( f'StringDataTypeDemo.Instances: {self.Instances}')
        print( f"Value: {value}")


title = "String Demo"
stringDemo = StringDataTypeDemo()

name = 'Shiva Sai'
stringDemo.displayDetails(title, name)

name = "Shiva Sai with Double Quotes"
stringDemo.displayDetails(title, name)

multilineString = """
                This is first line. \n
                This is second line.
"""
stringDemo.displayDetails("Multiline Demo", multilineString)

# concatenate with + operator, and repeated with *
chant = "Hare " + "Krishna "
stringDemo.displayDetails("+ Add Strings", chant)

# Two or more string literals next to each other are automatically concatenated.
chant = "Hare " "Krishna "
stringDemo.displayDetails("+ Add Strings", chant)

chant = "Hare Krishna " * 3
stringDemo.displayDetails("Multiply Strings", chant)

# to break long strings
longText = ('Put several strings within parentheses ' 
            'to have them joined together.')
stringDemo.displayDetails("Long Strings", longText)

