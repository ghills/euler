__author__ = 'gavin'


def get_divisors_sum(n):
    return sum(x for x in range(1, (n/2) + 1) if (n % x) == 0)

# first, build the list
sums = [get_divisors_sum(n=x) for x in xrange(1, 10000)]

running_total = 0
for i in xrange(1, 10000):
    if 0 < sums[i-1] < len(sums) and sums[i-1] != i and sums[sums[i-1]-1] == i:
        running_total += i
print running_total