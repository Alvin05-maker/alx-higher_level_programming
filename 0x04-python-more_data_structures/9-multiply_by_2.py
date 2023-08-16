#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiple_dir = a_dictionary.copy()
    list_keys = list(multiple_dir.keys())

    for idx in list_keys:
        multiple_dir[idx] *= 2

    return (multiple_dir)
