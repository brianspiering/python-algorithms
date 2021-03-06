#!/usr/bin/env python

""" Exploring code from Chapter 2 of Python Algorithms
"""

# Directly from book, p 26
# a, b, c, d, e, f, g, h = range(8)

# My work
# Assign in a more pythonic way
import string

for _ in xrange(8):
    exec(string.lowercase[_]+' = _')

# Back to code from book
N=[
 	{b, c, d, e, f},  #a
	{c, e},           #b
	{d},              #c
	{e},              #d
	{f},              #e
	{c, g, h},        #f
	{f, h},           #g
	{f, g}            #h
]

# p 27
b in N[a] # Neighborhood membership
len(N[f]) # Degree

# N=[
# 	[b, c, d, e, f], #a
# 	[c, e], #b
# 	[d], #c
# 	[e], #d
# 	[f], #e
# 	[c, g, h], #f
# 	[f, h], #g
# 	[f, g] #h
# ]

# N=[
# 	{b:2, c:1, d:3, e:9, f:4}, #a
# 	{c:4, e:3}, #b
# 	{d:8}, #c
# 	{e:7}, #d
# 	{f:5}, #e
# 	{c:2, g:2, h:2}, #f
# 	{f:1, h:6}, #g
# 	{f:9, g:8} #h
# ]

# N[a][b] # Edge weight for (a, b)

# N={
# 	'a': set('bcdef'),
# 	'b': set('ce'),
# 	'c': set('d'),
# 	'd': set('e'),
# 	'e': set('f'),
# 	'f': set('cgh'),
# 	'g': set('fh'),
# 	'h': set('fg')
# }

# N = [[0,1,1,1,1,1,0,0], # a 
# 	[0,0,1,0,1,0,0,0], # b 
# 	[0,0,0,1,0,0,0,0], # c 
# 	[0,0,0,0,1,0,0,0], # d 
# 	[0,0,0,0,0,1,0,0], # e 
# 	[0,0,1,0,0,0,1,1], # f 
# 	[0,0,0,0,0,1,0,1], # g 
# 	[0,0,0,0,0,1,1,0]] # h

# The Bunch pattern, page 34
from bunch import Bunch

x = Bunch(name="Jayne Cobb", position="Public Relations")

T = Bunch
t = T(left=T(left="a", right="b"), right=T(left="c"))