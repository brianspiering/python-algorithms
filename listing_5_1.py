#!/usr/bin/env python

""" Exploring code from Listing 5-1 on page 105 
"""

def walk(G, s, S=set()):
	""" Directly from Python Algorithms 
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