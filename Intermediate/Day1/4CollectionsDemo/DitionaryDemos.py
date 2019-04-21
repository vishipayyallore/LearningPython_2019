# Dictionary Data Type Demo
class DictDataTypeDemo:
    Instances = 0

    def __init__(self):
        DictDataTypeDemo.Instances += 1

    def displayDictionaryValues(self, title, value):
        try:
            print(f"----- {title} Length: {len(value)} -----")
            print(f'DictDataTypeDemo.Instances: {self.Instances}')
            print(f'{value}')
        except Exception as error:
            print("Error in DictDataTypeDemo::displaySetValues:", error)

    def displayIndividualElements(self, title, theSetOfElements):
        try:
            print(f"----- {title} -----")
            print(f'DictDataTypeDemo.Instances: {self.Instances}')
            for currentKey in theSetOfElements:
                print(f'{currentKey} = {theSetOfElements[currentKey]}')
        except Exception as error:
            print("Error in DictDataTypeDemo::displayIndividualElements:", error)


# --------------------------------------------------------------------------------
title = "Set Data Type Demo"

dictDataType = DictDataTypeDemo()

# Empty Dictionary
dictObject1 = {}
dictDataType.displayDictionaryValues(title, dictObject1)

friuts = {1: 'Apple', 2: 'Orange'}
dictDataType.displayDictionaryValues(title, friuts)

dictDataType.displayIndividualElements(title, friuts)