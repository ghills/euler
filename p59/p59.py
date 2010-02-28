#!/usr/bin/python

import string

dictionary = []

def check_list_words(l):
	for word in l:
		if word not in dictionary: return False
	return True

print "Project Euler -- Problem 59"
print "Brute force attempt to break an xor cipher\n\n"

f = open("cipher1.txt","r")

data = f.read().split(",")
# chomp off the newline
data[-1] = data[-1].rstrip()
f.close()

print "\nBuilding list of words from dictionary..."
f = open("/usr/share/dict/words","r")
for line in f:
	dictionary.append(line.rstrip().lower())
f.close()
print "Dictionary built.\n"

# convert to list of ints instead of strings
data = [ int(x) for x in data ]

# we know the key is 3 lower case letters, so try every combination
# and look at the first word to be in the english language
letter_vals = range(65,91)
letter_vals.extend(range(97,123))
pot = []
for i in string.ascii_lowercase:
	for j in string.ascii_lowercase:
		for k in string.ascii_lowercase:
			key = [i,j,k]
			#print "Key: %s" % "".join(key)
			c = 0
			words = []
			for t in range(0,6):
				new_word = ""
				while data[c] ^ ord(key[c % 3]) not in letter_vals:
					c += 1
				while data[c] ^ ord(key[c % 3]) in letter_vals:
					new_word += chr(data[c] ^ ord(key[c%3]))
					c += 1
				words.append(new_word)
			words = [ x.lower() for x in words ]
			if check_list_words(words):
				print "words found: %s" % " -- ".join(words)
				print "key added %s" % "".join(key)
				pot.append(key)

