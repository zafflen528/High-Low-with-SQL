import math as m
import random

import Main as M

RAND_NUM = random.randint(0,100) #result

def enter_name(name):
    print("Enter your name")
    name = input()

def score():
    res = hl()
    if res == 0:
        return 5000
    elif res == 1:
        return 1000
    else:
        return 500


def hl(): # the game itself
    print(RAND_NUM)
    num = int(input())
    diff = abs(RAND_NUM - num)
    if diff == 0:
        return 0
    elif diff <= 10:
        return 1
    elif diff > 10:
        return 2

