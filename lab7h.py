#!/usr/bin/env python3
# Student ID: [seneca_id]

# Function 1 accessing the global variable
def function1():
    print('print() in function1 on schoolName:', schoolName)

# Function 2 accessing the global variable
def function2():
    print('print() in function2 on schoolName:', schoolName)

# Defining the global variable schoolName
schoolName = 'Seneca College'

# Accessing global variable from the main script
print('print() in main on schoolName:', schoolName)

# Calling function1 and function2 which also access the global variable
function1()

# Accessing global variable again in the main script
print('print() in main on schoolName:', schoolName)

# Calling function2 to show global variable is accessible from multiple functions
function2()

# Finally, accessing the global variable in the main script
print('print() in main on schoolName:', schoolName)

