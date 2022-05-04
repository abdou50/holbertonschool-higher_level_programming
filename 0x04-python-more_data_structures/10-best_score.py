#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        for key in a_dictionary.keys():
            if a_dictionary[key] == max(list(a_dictionary.values())):
                return key
