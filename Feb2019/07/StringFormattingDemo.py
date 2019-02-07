# String Formatting Demo
class StringFormattingDemo:
    Instances = 0

    def __init__(self):
        StringFormattingDemo.Instances += 1

    def formatSingleString(self, title, value):
        try:
            print(
                f"----- {title} | Instances: {self.Instances}-----")
            print(f'StringFormattingDemo.Instances: {self.Instances}')
            print('{}'.format(value))
        except Exception as error:
            print("Error in StringFormattingDemo::formatSingleString:", error)

    def padSingleString(self, title, value, padNumber, padCharacter):
        try:
            formatString = f'{padCharacter}>{padNumber}s'
            print(
                f"----- {title} | Instances: {self.Instances}-----")
            print(f'StringFormattingDemo.Instances: {self.Instances}')
            print(format(value, formatString))
        except Exception as error:
            print("Error in StringFormattingDemo::padSingleString:", error)


# --------------------------------------------------------------------------------
title = "String Formatting Demo"
title1 = "Individual Display Demo"
formatString = StringFormattingDemo()

name = 'Shiva'
formatString.formatSingleString(title, name)

formatString.padSingleString(title, name, 10, '')
formatString.padSingleString(title, name, 10, '#')
