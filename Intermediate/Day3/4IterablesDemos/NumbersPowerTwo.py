class NumberPowerTwo:
    """Class to implement an iterator of powers of two
    """

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

number = 5
numberpower = NumberPowerTwo(number)
itr = iter(numberpower)

try:
    for i in range(1, number+3):
        print(next(itr))
except StopIteration:
    print(f'Stopping the loop.')

print('Using in for loop')
for val in NumberPowerTwo(number):
    print(val)