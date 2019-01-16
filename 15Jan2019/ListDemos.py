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

squares = [1, 4, 9, 16, 25]
listDemo.displayDetails(title, squares)

listDemo.displayDetails("List Slicing", squares[2:4]) 

listDemo.displayDetails("List Slicing", squares[:]) 

listDemo.displayDetails("List Concatenation", squares + integerList) 

