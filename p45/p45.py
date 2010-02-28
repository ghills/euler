#!/usr/bin/python

def tri(n):
	return n*(n+1)/2

def pent(n):
	return n*(3*n-1)/2

def hex(n):
	return n*(2*n-1)

print "Project Euler -- Problem 45"
print "Find next number after 40755 that is triangle, pentagonal, and hexagonal\n\n"

nt = 286
np = 166
nh = 144

while tri(nt) != pent(np) or pent(np) != hex(nh):
	if tri(nt) <= pent(np) and tri(nt) <= hex(nh):
		nt += 1
	elif pent(np) <= tri(nt) and pent(np) <= hex(nh):
		np += 1
	else:
		nh += 1

print "Solution: %d" % tri(nt)
print "nt: %d\tnp: %d\tnh: %d" % (nt,np,nh)
