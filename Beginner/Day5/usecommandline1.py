import sys

program_name = sys.argv[0]
arguments = sys.argv[1:]

count = len(arguments)

print(f'{program_name} {arguments} {count}')

for x in sys.argv:
    print( "Argument: ", x)
