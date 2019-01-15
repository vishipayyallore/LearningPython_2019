class ListDataTypeDemo:
    Instances = 0

    def __init__( self ):
        ListDataTypeDemo.Instances += 1

    def displayDetails( self, title, value ):
        print(f"----- {title} -----")
        print( f'ListDataTypeDemo.Instances: {self.Instances}')
        print( f"Length: {len(value)}")
        print( f"Value: {value}")

title = "List Data Type Demo"

listDemo = ListDataTypeDemo()

# Empty List
listOne = []
listDemo.displayDetails(title, listOne)

integerList = [10, 20, 30]
listDemo.displayDetails(title, integerList)

