#!/usr/bin/python3
"""json"""
import json


def load_from_json_file(filename):
    """create object"""
    with open(filename, mode='r', encoding="utf-8") as f:
        return(json.load(f))
