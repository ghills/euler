#!/usr/bin/python

def check_pal(s):
	return s == s[::-1]

def int2bin(n):
	bStr = ''
	if n < 0: raise ValueError, "must be a positive integer"
	if n == 0: return '0'
	while n > 0:
		bStr = str(n % 2) + bStr
		n = n >> 1
	return bStr

sum = 0
i = 1

print "Project Euler -- Problem #36"
print "Sum of all numbers less than one million that are palindromic in base 2 and 10"

print "Calculating........\n\n"
while i <= 1000000:
	if check_pal(str(i)) and check_pal(int2bin(i)): sum += i
	i += 1

print "Total: %s" % sum
