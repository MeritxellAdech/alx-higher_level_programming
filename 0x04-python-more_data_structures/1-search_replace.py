#!/usr/bin/python3
def search_replace(my_list, search, replace):
    rep_list = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            rep_list.append(replace)
            continue
        rep_list.append(my_list[i])
    return rep_list
