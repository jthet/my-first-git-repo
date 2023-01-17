"""
def add5_after_multiplying(value1, value2):
    return( (value1 * value2) + 5)

final_number = add5_after_multiplying(10, 2)
print(final_number)




def print_ts(mylist):
    for x in mylist:
        if (x[0] == 't'):      # a string (x) can be interpreted as a list of chars!
            print(x)

list1 = ['circle', 'heart', 'triangle', 'square']
list2 = ['one', 'two', 'three', 'four']

print_ts(list1)
print_ts(list2)


import names

for i in range(55):
    print(names.get_full_name())
"""

# Random number generator 1-100
import random

def getRand():
    for x in range(10):
        return(random.randrange(1, 100, 1))


def odd_or_even(totalNums):
    for x in range(totalNums):
        num = getRand()
        if (num % 2 == 0):
            print(f'{num} is Even')
        elif (True):
            print(f'{num} is Odd')

odd_or_even(30)