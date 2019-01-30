# Set Data Type Demo
class SetDataTypeDemo:
    Instances = 0

    def __init__(self):
        SetDataTypeDemo.Instances += 1

    def displaySetValues(self, title, value):
        try:
            print(f"----- {title} Length: {len(value)} -----")
            print(f'SetDataTypeDemo.Instances: {self.Instances}')
            print(f'{value}')
        except Exception as error:
            print("Error in SetDataTypeDemo::displaySetValues:", error)

    def displayType(self, title, theObject):
        try:
            print(f"----- {title} -----")
            print(f'SetDataTypeDemo.Instances: {self.Instances}')
            print(f'{type(theObject)}')
        except Exception as error:
            print("Error in SetDataTypeDemo::displaySetValues:", error)


title = "Set Data Type Demo"

setDataType = SetDataTypeDemo()

oddNumbers = {1, 3, 5, 7, 9}
evenNumbers = {2, 4, 6, 8, 0}

setDataType.displaySetValues(title, oddNumbers)
setDataType.displaySetValues(title, evenNumbers)
setDataType.displaySetValues(title, (oddNumbers | evenNumbers))

setDataType.displaySetValues("Union", oddNumbers.union(evenNumbers))
setDataType.displaySetValues("Intersection", oddNumbers.intersection(evenNumbers))
#setDataType.displaySetValues("Union", oddNumbers.union(evenNumbers))
#setDataType.displaySetValues("Union", oddNumbers.union(evenNumbers))
