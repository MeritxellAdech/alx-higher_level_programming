#!/usr/bin/python3

def remove_char_at(str, n):
    strlen = len(str)
    if n > strlen or n < 0 or str == "":
        return str
    s = ""
    for i in str:
        if i == str[n]:
            continue
        s += i
    return s
