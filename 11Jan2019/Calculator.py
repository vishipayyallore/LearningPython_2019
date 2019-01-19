class DataTypesDemo:
    Instances = 0

    def __init__(self):
        DataTypesDemo.Instances += 1

    def displayDetails(self, title, value):
        print(f"----- {title} -----")
        print(f'DataTypesDemo.Instances: {self.Instances}')
        print(f"{title}{value}")


operationTitle = "Division Output: "
type1 = DataTypesDemo()

operationOutput = 5/3  # Returns float
type1.displayDetails(operationTitle, operationOutput)

operationOutput = 5//3  # // Returns int part ignoring fractional part
type1.displayDetails(operationTitle, operationOutput)

operationTitle = "(**) Power Operator : "
operationOutput = 5 ** 2  # 5 to the Power of 2
type1.displayDetails(operationTitle, operationOutput)

operationOutput = 5 ** 7  # 5 to the Power of 7
type1.displayDetails(operationTitle, operationOutput)
