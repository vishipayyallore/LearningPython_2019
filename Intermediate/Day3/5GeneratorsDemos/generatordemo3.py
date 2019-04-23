def NumberPowerTwo(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

number = 5

print('Using in for loop')
for val in NumberPowerTwo(number):
    print(val)