# Fibonacci series

first, second = 0, 1

while first < 10:
    print(first)
    print(f'----- {first} {second} -----')
    first, second = second, first+second

