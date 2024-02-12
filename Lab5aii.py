#!/usr/bin/env python3

import sys 
if len(sys.argv) !=3:
    print(f'Usage: {sys.argv[0]} <name> <age> ')
    sys.exit(1)

else:
    print("Input three arguments in the command line")


# Assign the first command-line arguement to the string object called "name"
name = sys.argv[1]

# Assign the Second command-line arguement to the integar object called "age
# "
age = sys.argv[2]

# A print statement that says the below

print('Hi ' + (str(sys.argv[1])) + ','  ' you are ' +(str(int(sys.argv[2]))) + ' years old' 
)
def helloWorld():
	print(‘Hello World’)


helloWorld()

