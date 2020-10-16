from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)

fact = fact()
x = 0
for el in fact:
    if x < 6:
        print(el)
        x += 1
    else:
        break