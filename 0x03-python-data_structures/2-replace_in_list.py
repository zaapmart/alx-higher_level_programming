#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return(my_list)

vi 3-print_reversed_list_integer.py

#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for i in reversed(my_list):
        print('{:d}'.format(i))
