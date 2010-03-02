#!/usr/bin/python

print "Project Euler -- Problem 12"
print "First triangle number with  over 500 divisors\n\n"

def num_divisors(n):
	count = 0
	for i in range(1,n+1):
		if n % i == 0: count +=1
	return count

n = 10

while num_divisors(n*(n+1)/2) <= 500: n += 1

print "Solution: %d" % n


