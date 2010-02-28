#!/usr/bin/python

def check_pal(s):
	return s == s[::-1]

def rev_int(n):
	return (int)(str(n)[::-1])

count = 0

print "Project Euler -- Problem #55"
print "Find all Lychrel numbers less than 10000"
print "A number that added to itself reversed does not form a palindrome (in 50 iterations\n\n"

for i in range(1,10000):
	# assume it is Lychrel until proved otherwise
	count += 1
	val = i
	j = 0
	while j < 50:
		val = val + rev_int(val)
		if check_pal(str(val)):
			count -= 1
			j = 51
		j += 1


print "Total: %d" % count



