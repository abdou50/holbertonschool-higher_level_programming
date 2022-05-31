#!/usr/bin/python3
""" hihihih """
import json


def load_from_json_file(filename):
    """class"""
    with open(filename, encoding="Utf-8") as fk:
        return json.load(fk)
