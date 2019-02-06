# Dictionary Data Type Demo
class DictDataTypeDemo:
    Instances = 0

    def __init__(self):
        DictDataTypeDemo.Instances += 1

    def displayDictionaryValues(self, title, value):
        try:
            print(
                f"----- {title} | Length: {len(value)} | Instances: {self.Instances}-----")
            print(f'DictDataTypeDemo.Instances: {self.Instances}')
            print(f'{value}')
        except Exception as error:
            print("Error in DictDataTypeDemo::displaySetValues:", error)

    def displayIndividualElements(self, title, theSetOfElements):
        try:
            print(f"----- {title} | Instances: {self.Instances} -----")
            for currentKey in theSetOfElements:
                print(f'{currentKey} = {theSetOfElements[currentKey]}')
        except Exception as error:
            print("Error in DictDataTypeDemo::displayIndividualElements:", error)


# --------------------------------------------------------------------------------
title = "Dictionary Data Type Demo"
title1 = "Individual Display Demo"
dictDataType = DictDataTypeDemo()

# Empty Dictionary
emptyDict = {}
dictDataType.displayDictionaryValues(title, emptyDict)
dictDataType.displayIndividualElements(title1, emptyDict)

friuts = {1: 'Apple', 2: 'Orange'}
dictDataType.displayDictionaryValues(title, friuts)
dictDataType.displayIndividualElements(title1, friuts)

family = {'id': 1, 'name': "Shiva", 'salary': 12345.67,
          'subjects': ['CSharp', 'Angular']}
dictDataType.displayDictionaryValues(title, family)
dictDataType.displayIndividualElements(title1, family)

# from dict() method
friuts = dict({1: 'Apple', 2: 'Orange', 3: 'Grapes'})
dictDataType.displayDictionaryValues(title, friuts)
dictDataType.displayIndividualElements(title1, friuts)

# from dict() method using Tuples
friuts = dict([(1, 'Apple'), (2, 'Orange'), (3, 'Grapes'), (4, 'Mango'), (5, 'Pine Apple')])
dictDataType.displayDictionaryValues(title, friuts)
dictDataType.displayIndividualElements(title1, friuts)
