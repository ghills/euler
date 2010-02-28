#!/usr/bin/python

import string

print "Project Euler -- Problem 59"
print "Decrypt the file and print out the ascii total\n\n"

f = open("cipher1.txt","r")

data = f.read().split(",")
# chomp off the newline
data[-1] = data[-1].rstrip()
f.close()

# convert to list of ints instead of strings
data = [ int(x) for x in data ]

# open other file for writing
f = open("cleartext.txt","w")

# key found from other brute force breaker
key = ['g','o','d']

clr = []

sum = 0
for i in range(0,len(data)):
	num = data[i] ^ ord(key[i % 3])
	ltr = chr(num)
	sum += num
	clr.append(ltr)

f.write("".join(clr))
print "Sum: %d" % sum

f.close()

