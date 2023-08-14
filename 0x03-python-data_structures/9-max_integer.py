#!/user/bin/python3

def max_integer(my_list=[]):
    maximum = my_list[0]
    for index in range(len(my_list)):
        if my_list[index] > my_list[0]:
            maximum = my_list[index]
            return maximum
