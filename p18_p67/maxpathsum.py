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
    def __init__(self, value, leftbest=0, rightbest=0):
        self.value = value
        self.leftbest = leftbest
        self.rightbest = rightbest

def MaxPathSum(triangle):
    triangle = [[Node(value=x) for x in row] for row in triangle]
    triangle.reverse()
    for row, nextrow in izip(triangle, triangle[1:]):
        for i, node in enumerate(row):
            best_to_here = max(node.leftbest, node.rightbest)
            if i > 0:
                nextrow[i - 1].rightbest = node.value + best_to_here
            if i < len(row) - 1:
                nextrow[i].leftbest = node.value + best_to_here
    top_node = triangle[-1][0]
    return top_node.value + max(top_node.leftbest, top_node.rightbest)

filename = sys.argv[1]

triangle_data = [ [int(x) for x in l.strip().split(' ')] for l in open(filename, 'r') ]
print 'rows: ', len(triangle_data)
print 'max path sum: ', MaxPathSum(triangle_data)

