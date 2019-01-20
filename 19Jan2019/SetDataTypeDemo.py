# Set Data Type Demo
class SetDataTypeDemo:
    Instances = 0

    def __init__(self):
        SetDataTypeDemo.Instances += 1

    def displaySetValues(self, title, value):
        print(f"----- {title} -----")
        print(f'SetDataTypeDemo.Instances: {self.Instances}')
        print(f'----- {value} -----')

title = "Set Data Type Demo"

setDataType = SetDataTypeDemo()

numbersSet = { 3, 7, 11, 15 }
setDataType.displaySetValues(title, numbersSet)
