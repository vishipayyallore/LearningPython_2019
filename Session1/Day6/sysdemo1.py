#!/usr/bin/env python3

import sys

print(f'Executable: {sys.executable}')
print(f'Version: {sys.version}')
print(f'Perfix: {sys.prefix}')
print(f'Path: {sys.path}')

counter = 0
for arg in sys.argv:
    print(f'Arg[{counter}]: {sys.argv[counter]}')
    counter += 1

