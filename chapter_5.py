#!/usr/bin/env python

""" Exploring code from Chapter 2 of Python Algorithms
"""

def walk(G, s, S=set()):
	""" Directly from book, p 105
	"""
	P, Q = dict(), set()
	P[s] = None
	Q.add(s)
	while Q:
		u = Q.pop()
		for v in G[u].difference(P, S):
			Q.add(v)
			P[v] = u
	return P