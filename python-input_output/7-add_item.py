#!/usr/bin/python3
"""script"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

fname = "add_item.json"
List = []

try:
    List = load_from_json_file(fname)
except:
    pass

for i in range(1, len(sys.argv)):
    List.append(sys.argv[i])
save_to_json_file(List, fname)
