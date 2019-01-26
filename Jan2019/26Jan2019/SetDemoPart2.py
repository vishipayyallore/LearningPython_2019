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


title = "Set Data Type Demo"
title1 = "Identify Data Type Demo"

setDataType = SetDataTypeDemo()

# Empty Set
emptySet = {}
emptySet1 = set()

setDataType.displayType(title1, emptySet)
setDataType.displayType(title1, emptySet1)

vars = locals()
print(vars)
for k, v in vars.items():
        print(f'{k} = {k}')
