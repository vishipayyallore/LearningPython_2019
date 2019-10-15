full_name = "Shiva Sai"

print(full_name[::-1])

for value in range(1, 5):
    if(value % 10 == 0):
        break
    print(value, end=' | ')
else:
    print('I will be seen!')


number = 5
while(number >= 0):
    print(number, end=' ^ ')
    number -= 1
else:
    print('I will be seen!')