def reverse_string(string_data):
    for ictr in range( (len(string_data) - 1), -1, -1):
        yield string_data[ictr]

for char in reverse_string("hello"):
    print(char)
