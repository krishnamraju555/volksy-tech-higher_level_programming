#!/usr/bin/python3
"""append"""


def append_write(filename="", text=""):
    """Adding to text"""
    if filename:
        with open(filename, mode='a', encoding="utf-8")as f:
            return(f.write(text))
