#!/usr/bin/python

print "Project Euler -- Problem 11"

f = open("grid.txt","r")

nums = [ [int(n.rstrip()) for n in s.split(" ")] for s in f.readlines() ]

omax = 0

for i in range(0,20):
	for j in range(0,20):
		#up
		lmax = 0
		if i >= 3:
			lmax = nums[i][j]*nums[i-1][j]*nums[i-2][j]*nums[i-3][j]
		omax = max(lmax,omax)

		#down
		lmax = 0
		if i <= 16:
			lmax = nums[i][j]*nums[i+1][j]*nums[i+2][j]*nums[i+3][j]
		omax = max(lmax,omax)

		#left
		lmax = 0
		if j >= 3:
			lmax = nums[i][j]*nums[i][j-1]*nums[i][j-2]*nums[i][j-3]
		omax = max(lmax,omax)

		#right
		lmax = 0
		if j <= 16:
			lmax = nums[i][j]*nums[i][j+1]*nums[i][j+2]*nums[i][j+3]
		omax = max(lmax,omax)

		#diaganol
		lmax = 0
		if j <= 16 and i <= 16:
			lmax = nums[i][j]*nums[i+1][j+1]*nums[i+2][j+2]*nums[i+3][j+3]
		omax = max(lmax,omax)

		#diaganol 2
		lmax = 0
		if j <= 16 and i >= 3:
			lmax = nums[i][j]*nums[i-1][j+1]*nums[i-2][j+2]*nums[i-3][j+3]
		omax = max(lmax,omax)

print "Max value is: %d" % omax

f.close()
