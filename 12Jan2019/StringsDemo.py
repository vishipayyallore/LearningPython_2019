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



