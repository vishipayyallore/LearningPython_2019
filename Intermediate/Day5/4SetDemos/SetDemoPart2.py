# Set Data Type Demo
class SetDataTypeDemo:
    Instances = 0

    def __init__(self):
        SetDataTypeDemo.Instances += 1

    def displaySetValues(self, title, value):
        print(f"----- {title} -----")
        print(f'SetDataTypeDemo.Instances: {self.Instances}')
        print(f'{value}')

    def displayType(self, title, theObject):
        print(f"----- {title} -----")
        print(f'SetDataTypeDemo.Instances: {self.Instances}')
        print(f'{type(theObject)}')

def main():
    title = "Set Data Type Demo"
    title1 = "Identify Data Type Demo"

    setDataType = SetDataTypeDemo()

    # Empty Set
    emptySet = {}
    emptySet1 = set()

    setDataType.displayType(title1, emptySet)
    setDataType.displayType(title1, emptySet1)

    # Adding an element to the set
    emptySet1.add(9)
    emptySet1.add(12)

    # Adding Multiple values
    emptySet1.update({"Shiva", "Sai"})
    emptySet1.update({12.34, 23.57})

    # list and a set as elements
    emptySet1.update({"Shiva", "Sai"}, {92.56, 56.45, 78.45, 12.34})

    setDataType.displaySetValues(title, emptySet1)

if __name__ == "__main__":
    main()
