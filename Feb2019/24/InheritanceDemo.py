# Inheritance "is a " Relationship
class Shape:
    Instances = 0

    def __init__(self, area):
        Shape.Instances += 1
        self.__area__ = area

    def displayDetails(self):
        try:
            print(f"----- Shape | Instances: {self.Instances}-----")
            print('{}'.format(self.__area__))
        except Exception as error:
            print("Error in Shape::formatSingleString:", error)


# --------------------------------------------------------------------------------
shapeDemo = Shape(2)
shapeDemo.displayDetails()
