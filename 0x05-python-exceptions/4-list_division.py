#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for i in range(0, list_length):
        try:
            list_div = my_list_1[i]/my_list_2[i]
        except TypeError:
            print("wrong type")
            list_div = 0
        except ZeroDivisionError:
            print("division by 0")
            list_div = 0
        finally:
            newList.append(list_div)

        return (newList)
