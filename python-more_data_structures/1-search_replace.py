#!/usr/bin/python3
def search_replace(my_list, search, replace):
    li = my_list[:]
    for i in range(len(li)):
        if li[i] == search:
            li[i] = replace
    return li
