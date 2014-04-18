#!/usr/bin/python

import sys

from itertools import izip

def DumbPathSum(triangle, row, idx):
    # recursive brute force solution
    # like a simple recursive fibonacci algorithm, recalcs the same thing many
    # times over
    if row == len(triangle) - 1:
        return triangle[row][idx]
    else:
        return triangle[row][idx] + \
                max( DumbPathSum(triangle, row + 1, idx ),
                     DumbPathSum(triangle, row + 1, idx + 1) )

class Node(object):
    __slots__ = ['value', 'maxpath']
    def __init__(self, value, maxpath):
        self.value = value
        self.maxpath = maxpath

def MaxPathSum(triangle):
    triangle = [[Node(value=x, maxpath=x) for x in row] for row in triangle]
    triangle.reverse()
    for row, prevrow in izip(triangle[1:], triangle):
        for i, node in enumerate(row):
            node.maxpath = node.value + max(prevrow[i].maxpath, prevrow[i+1].maxpath)
    return triangle[-1][0].maxpath

filename = sys.argv[1]

triangle_data = [ [int(x) for x in l.strip().split(' ')] for l in open(filename, 'r') ]
print MaxPathSum(triangle_data)

