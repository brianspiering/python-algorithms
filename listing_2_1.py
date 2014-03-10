#!/usr/bin/env python

""" Exploring code from Listing 2-1 on page 26 
"""

# Directly from book 
# a, b, c, d, e, f, g, h = range(8)

# My work
# Assign in a more pythonic way
import string

for i in xrange(8): # TODO: Make into one-liner
    exec(string.lowercase[i]+' = i') 
    
# Back to code from book
