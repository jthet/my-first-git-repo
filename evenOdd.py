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

odd_or_even(10)