def generate_789():
    
    n = 7
    print(f'Returning {n}')
    # Generator function contains yield statements
    yield n

    n += 1
    print(f'Returning {n}')
    yield n

    n += 1
    print(f'Returning {n}')
    yield n


number = 4
try:
    gen = generate_789()
    for i in range(1, number+3):
        print(next(gen))
except StopIteration:
    print(f'Stopping the loop.')


# Using for loop
for item in generate_789():
    print(item)
