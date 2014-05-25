#!/usr/bin/env python

""" Explore Chapter 6 of Python Algorithms

Heaps and Greedy Algorithms 
"""

# from p 158
from heapq import heapify, heappush, heappop
from itertools import count

def huffman(seq, frq):
    num = count()
    trees = list(zip(frq, num, seq))
    heapify(trees)
    while len(trees) > 1:
        fa, _, a = heappop(trees)
        fb, _, b = heappop(trees)
        n = next(num)
        heappush(trees, (fa+fb, n, [a, b]))
    return trees[0][-1]

seq_book = "abcdefghi"
frq_book = [4, 5, 6, 9, 11, 12, 15, 16, 20]
tree_book = huffman(seq, frq)

# my version
import string
import random

n = 10
seq_mine = string.letters[:n]
frq_mine = [random.randint(1, 10) for _ in xrange(n)]
tree_mine = huffman(seq, frq)