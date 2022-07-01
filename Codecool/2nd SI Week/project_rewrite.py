import heapq
from itertools import count
from re import L
from unittest import result


x = input("first number: ")
y = input("second number: ")

def min(x, y):
    if x > y:
        return y
    else:
        return x
print(min(x, y))

values_list = [1, 5, 6, 14, 25, 110, 3, 7]
def max(values_list):
    highest_number = 0
    for number in values_list:
        if number > highest_number:
            highest_number = number
    return highest_number
print(max(values_list))




def len(values_list):
    count = 0
    for element in values_list:
        count += 1
    return count
print(len(values_list))

x = int(input())
y = int(input())
def multiply(x, y):
    if (y == 0):
        return 0
    elif (y > 0):
        return(x + multiply(x, y -1))
    elif (y < 0):
        return -multiply(x, -y)
print(multiply(x, y))

def pow(x, y):
    result = 1
    for i in range(1, y + 1):
        result = result * x
        return result
print(pow(x, y))


def divmod(x, y):
    pass