#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    a = 0
    b = 0
    total = 0
    sumset = 0
    for s in my_list:
        a = s[0]
        b = s[1]
        total += b
        sumset += (a * b)
    return (sumset / total)
