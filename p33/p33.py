#!/usr/bin/python

print "Project Euler -- Problem 33"
print "Fractions with the curious cancellation property\n\n"

def is_curious(frac):
	if frac[0] % 10 == 0 and frac[1] % 10 == 0:
		return False #trivial case

	n = 1
	d = 1

	# cx / yc
	if (frac[0] / 10) == (frac[1] % 10):
		n = frac[0] % 10
		d = frac[1] / 10
	# xc / cy
	if (frac[0] % 10) == (frac[1] / 10):
		n = frac[0] / 10
		d = frac[1] % 10
	# cx / cy
	if (frac[0] / 10) == (frac[1] / 10):
		n = frac[0] % 10
		d = frac[1] % 10
	# xc / yc
	if (frac[0] % 10) == (frac[1] % 10):
		n = frac[0] / 10
		d = frac[1] / 10

	if (d == 0): return False

	return float(frac[0]) / frac[1] == float(n) / d


results = []
for i in range(10,100):
	for j in range(10,i):
		if is_curious([j,i]):
			results.append([j,i])

print "Found %d answers" % len(results)
print results
