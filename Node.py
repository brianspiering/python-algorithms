#!/usr/bin/env python

""" Exploring code from "BLACK BOX: LIST" on page 11
"""

class Node:
	""" Directly from book  
	"""
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# Still directly from book
L = Node("a", Node("b", Node("c", Node("d"))))
# print(L.next.next.value)

# My work
print("'%s' is the 1st item in linked list.") % (L.value)
print("'%s' is the 2nd item in linked list") % (L.next.value)

# TODO: walk through linked list to find all values
