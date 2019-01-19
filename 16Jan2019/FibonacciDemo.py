# Fibonacci series


class FibonacciSeriesDemo:
    Instances = 0

    def __init__(self):
        FibonacciSeriesDemo.Instances += 1

    def displayFibonacci(self, title, value):
        first, second = 0, 1
        print(f"----- {title}till {value} -----")
        print(f'FibonacciSeriesDemo.Instances: {self.Instances}')
        while first < value:
            print(first)
            # print(f'----- {first} {second} -----')
            first, second = second, first+second


title = "Fibonacci Series Demo"

fibonacci = FibonacciSeriesDemo()
fibonacci.displayFibonacci(title, 10)

fibonacci.displayFibonacci(title, 20)

# first, second = 0, 1

# while first < 10:
# print(first)
# print(f'----- {first} {second} -----')
# first, second = second, first+second
