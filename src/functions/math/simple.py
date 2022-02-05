#!/usr/bin/env python

def add(*args):
    result = 0
    for n in range(len(args)):
        result += args[n]
    return result
