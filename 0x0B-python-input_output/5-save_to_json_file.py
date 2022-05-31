#!/usr/bin/python3
""" hihihih """
import json


def save_to_json_file(my_obj, filename):
    """class"""
    with open(filename, mode="w", encoding="UTF-8") as files:
        json.dump(my_obj, files)
