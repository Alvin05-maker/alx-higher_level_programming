#!/usr/bin/python3
"""Define a list division"""


def list_division(my_list_1, my_list_2, list_length):
    """ Representation of the list division function .

    Args:
        my_list_1(int): first list
        my_list_2(int): second list
    """
    newList = []
    for i in range(list_length):
        try:
            list_div = my_list_1[i]/my_list_2[i]
        except IndexError:
            print("out of range")
            list_div = 0
        except TypeError:
            print("wrong type")
            list_div = 0
        except ZeroDivisionError:
            print("division by 0")
            list_div = 0
        finally:
            newList.append(list_div)
    return (newList)
