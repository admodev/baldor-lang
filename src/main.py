#!/usr/bin/env python

# Baldor, practical, functional, mathematical.

from functions.math import *

# Demonstration of functions with variable number of arguments:
add(2, 5, 2, 4)
subtract(4, 2, 2)
multiply(2, 2, 8, 10)
divide(1, 3, 5, 7, 2, 4)

# Demonstration of the practicity to call a simple method to calculate something with just a single keyword and a parameter:
x = sqroot(4)
y = sqroot(8)
z = sqroot(42)
print(x, y, z)
