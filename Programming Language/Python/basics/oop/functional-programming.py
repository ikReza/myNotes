# -*- coding: utf-8 -*-
"""
pure function:
    1. Give same output for same input
    2. Doesn't have any side effect
"""

def multiplyBy2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    
    return new_list

#print(multiplyBy2([1, 2, 3]))

# The above function have no side effect. But how can we write with side effect?
# We're using "print" method inside of the below function
"""
def multiplyBy2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    
    return print(new_list)

multiplyBy2([1, 2, 3])
"""
############################################################################

# map(function, iterables)
# Exapmple-1
def myFunc(n):
    return len(n)

x = map(myFunc, ("apple", "jackfruit", "cauliflower"))
print(x)
#convert the map into a list, for readability:
print(list(x))

# Example-2
def myFunc2(a, b):
    return a + b

x = map(myFunc2, ("apple", "banana"), ("red", "yellow"))
print(list(x))

##########################################################################

# zip
my_list = [1, 2, 3]
your_list = [10, 20, 30]
her_tuple = (100, 200, 300)
print(list(zip(my_list, your_list)))
print(list(zip(my_list, her_tuple)))
print(list(zip(my_list, your_list, her_tuple)))

#########################################################################
# accumulator
from functools import reduce

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, [i for i in range(5)], 0))

#########################################################################
# Lambda expressions
my_list = [1, 3, 5]
print(list(map(lambda item: item*2, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))
