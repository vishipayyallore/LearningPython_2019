names = ["shiva", "sai", "azim", "mathews", "philips", "samule"]

items = [name.capitalize() for name in names]
print(items)

items = [len(name) for name in names]
print(items)


string = "Shiva1 Sai2 Azim3 4 5"
numbers = [x for x in string if x.isdigit()]
print(numbers)

def get_list_comprehensions(lambda_expression, value):
    return [lambda_expression(x) for x in range(value)]

data = get_list_comprehensions(lambda x: x*2, 12)
print(data)

data = get_list_comprehensions(lambda x: x**2, 12)
print(data)