#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    moy = 0
    all = 0
    for i in my_list:
        moy += i[0] * i[1]
        all += i[1]
    return float(moy / all)
