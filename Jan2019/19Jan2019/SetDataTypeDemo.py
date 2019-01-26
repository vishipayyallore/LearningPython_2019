# Set Data Type Demo
class SetDataTypeDemo:
    Instances = 0

    def __init__(self):
        SetDataTypeDemo.Instances += 1

    def displaySetValues(self, title, value):
        print(f"----- {title} -----")
        print(f'SetDataTypeDemo.Instances: {self.Instances}')
        print(f'{value}')

title = "Set Data Type Demo"

setDataType = SetDataTypeDemo()

# set can't store duplicate
numbersSet = { 3, 7, 11, 15, 15, 15 }
setDataType.displaySetValues(title, numbersSet)

# Mixed data types set
mixedDataSet = {11, 1.1, "11", (1, 2)}
setDataType.displaySetValues(title, mixedDataSet)

# using set() method
mixedDataSet1 = set([11, 1.1, "11", "Shiva", (1, 2)])
setDataType.displaySetValues(title, mixedDataSet1)

listData = [11, 1.1, "11", "Shiva Sai", (1, 2)]
listData.append("Rajesh")
setDataType.displaySetValues("Display List", listData)

mixedDataSet2 = set(listData) 
setDataType.displaySetValues(title, mixedDataSet2)
