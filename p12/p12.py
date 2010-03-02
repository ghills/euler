#!/usr/bin/python

print "Project Euler -- Problem 12"
print "First triangle number with  over 500 divisors\n\n"

import operator
# A slightly efficient superset of primes.
def PrimesPlus():
	yield 2
	yield 3
	i = 5
	while True:
		yield i
		if i % 6 == 1:
			i += 2
		i += 2

# Returns a dict d with n = product p ^ d[p]
def GetPrimeDecomp(n):
	d = {}
	primes = PrimesPlus()
	for p in primes:
		while n % p == 0:
			n /= p
			d[p] = d.setdefault(p, 0) + 1
		if n == 1:
			return d

def num_divisors(n):
	d = GetPrimeDecomp(n)
	powers_plus = map(lambda x: x+1, d.values())
	return reduce(operator.mul, powers_plus, 1)

n = 10

while num_divisors(n*(n+1)/2) < 500: n += 1

print "Solution: %d" % (n*(n+1)/2)


