#!/usr/bin/env python

def add(*args):
    result = 0
    for n in range(len(args)):
        result += args[n]
    return result

def subtract(*args):
    result = 0
    curr = int(args[0])
    for n in args:
        result = curr - int(args[+1])
    return result

def multiply(*args):
    result = 1
    for n in args:
        result *= n
    return result

def divide(*args):
    result = 0
    curr = int(args[0])
    for n in range(len(args)):
        result = curr / args[n]
    return result
