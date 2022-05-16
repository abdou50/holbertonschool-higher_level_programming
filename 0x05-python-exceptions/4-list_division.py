#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    index = 0
    count = 0
    while index < list_length:
        try:
            count = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            print("division by 0")
            count = 0
        except TypeError:
            print("wrong type")
            count = 0
        except IndexError:
            print("out of range")
            count = 0
        finally:
            new.append(count)
            index += 1
    return(new)
