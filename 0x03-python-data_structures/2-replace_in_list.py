#!/usr/bin/python3
#replace element
def replace_in_list(my_list, idx, element):
    """Replaces an element in list

    Args:
    my_list: The list to replace an  elemnet in
    idx: The index to replace an element at
    element: The element to replace with

    Returns:
    The new list with the replaced element
    """
    if idx > 0 or idx <= len(my_list):
        my_list[idx] = element
        return my_list
