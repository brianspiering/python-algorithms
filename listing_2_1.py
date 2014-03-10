#!/usr/bin/env python

""" Exploring code from Listing 2-1 on page 26 
"""

# Directly from book 
# a, b, c, d, e, f, g, h = range(8)

# My work
# Assign in a more pythonic way
import string

for _ in xrange(8): # TODO: Make into one-liner
    exec(string.lowercase[_]+' = _') 
    
# Back to code from book
N=[
{b, c, d, e, f}, #a
{c, e}, #b
{d}, #c 
{e}, #d 
{f}, #e 
{c, g, h}, #f
{f, h}, #g
{f, g} #h
]

b in N[a] # Neighborhood membership
len(N[f]) # Degree