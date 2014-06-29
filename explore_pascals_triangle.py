#!/usr/bin/env python
# -*- coding: utf-8 -*-

from memo import memo

"""Explore Pascal’s Triangle
From Python Algorithms by Magnus Lie Hetland, page 179-181
"""

@memo
def C(n, k):
    """ Pascal's triangle number calculator. Direct from book"""
    if k == 0: return 1
    if n == 0: return 0
    return C(n-1, k-1) + C(n-1, k)

# Refactor for readability
@memo
def calc_pascal_value(row_id, col_id):
    """Calculate next value for Pascal’s triangle."""
    if col_id == 0: return 1
    if row_id == 0: return 0
    return calc_pascal_value(row_id-1, col_id-1) +\
           calc_pascal_value(row_id-1, col_id)
