
numbers = [i for i in range(1,11)]
print(numbers)

numbers = [i*2 for i in range(1,11)]
print(numbers)

numbers = [i*i*i for i in range(1,11)]
print(numbers)


numbers = [i for i in range(1,11) if i%2 == 0]
print(numbers)

numbers = [i for i in range(1,11) if i%2 != 0]
print(numbers)

numbers = [i**2 for i in range(1,11)]
print(f'Squares: {numbers}')
