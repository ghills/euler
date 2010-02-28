#!/usr/bin/python

print "Project Euler -- Problem 59"
print "Brute force attempt to break an xor cipher\n\n"

f = open("cipher1.txt","r")

data = f.read().split(",")
# chomp off the newline
data[-1] = data[-1].rstrip()
f.close()

# convert to list of ints instead of strings
data = [ int(x) for x in data ]

# we know the key is 3 lower case letters, so try every combination
# and look at the first word to be in the english language

