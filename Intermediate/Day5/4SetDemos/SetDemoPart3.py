# Set Data Type Demo
class SetDataTypeDemo:
    Instances = 0

    def __init__(self):
        SetDataTypeDemo.Instances += 1

    def displaySetValues(self, title, value):
        try:
            print(f"----- {title} -----")
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

def main():
        
    title = "Set Data Type Demo"
    title1 = "Identify Data Type Demo"

    setDataType = SetDataTypeDemo()

    newSetValues = {22, 33, 55, 77, 99}
    setDataType.displaySetValues(title, newSetValues)
    setDataType.displayType(title1, newSetValues)

    # Removing element
    newSetValues.discard(22)
    setDataType.displaySetValues(title, newSetValues)

    newSetValues.pop()
    setDataType.displaySetValues(title, newSetValues)

    newSetValues.pop()
    setDataType.displaySetValues(title, newSetValues)

    newSetValues.clear()
    setDataType.displaySetValues(title, newSetValues)


if __name__ == "__main__":
    main()