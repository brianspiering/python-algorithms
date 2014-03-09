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

# Walk through linked list
for i in xrange(10): # TODO: make a while loop

	location = "L."+"next."*i+"value" # Find based number of nexts/links

	try: 		
		print("'%s' is the number %d item in linked list.") % (eval(location), i+1)
	except:
		# print "past end of linked list"
		break