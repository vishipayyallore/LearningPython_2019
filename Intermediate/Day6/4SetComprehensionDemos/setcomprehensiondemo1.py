from math import factorial

factorials_list = [factorial(x) for x in range(10)]
print(factorials_list)

# Removes the duplicate
factorials_list = {factorial(x) for x in range(10)}
print(factorials_list)

