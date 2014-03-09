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
# print("'%s' is the 1st item in linked list.") % (L.value)
# print("'%s' is the 2nd item in linked list") % (L.next.value)
# print("'%s' is the 4nd item in linked list") % (L.next.next.next.value)
# L = Node("a") # Shorted linked list
# L = Node("a", Node("b", Node("c", Node("d", Node("e"))))) # Longer linked list

# Walk through the linked list
for i in xrange(10000000000000000): # A kludge, the linked list will never be that big

	location = "L."+"next."*i+"value" # Find location based number of nexts/links

	try: 		
		print("'%s' is item number %d in linked list.") % (eval(location), i+1)
	except AttributeError:
		# print "Past end of current linked list."
		break