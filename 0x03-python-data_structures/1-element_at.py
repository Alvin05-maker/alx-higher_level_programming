#!/usr/bin/python3
""" Return the element of a list 
at a given index"""
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    else:
        for index in range(len(my_list)):
            return (my_list[idx])
