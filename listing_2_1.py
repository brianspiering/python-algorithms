#!/usr/bin/env python

""" Exploring code from Listing 2-1 on page 26 
"""

# Directly from book 
a, b, c, d, e, f, g, h = range(8)

# My work
# Assign in a more pythonic way
import string

letters = list(string.lowercase[0:8]) 
