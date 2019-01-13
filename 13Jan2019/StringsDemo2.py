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

name = "Shiva Sai"
stringDemo.displayDetails(title, name)

# Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; 
stringDemo.displayDetails(title, name[0])

# Indices may also be negative numbers, to start counting from the right. negative indices start from -1.
stringDemo.displayDetails(title, name[-3] + name[-2] + name[-1] )

