__author__ = 'gavin'
import itertools


def get_divisors_sum(n):
    return sum(x for x in range(1, (n/2) + 1) if (n % x) == 0)

abundant = set(i for i in xrange(1, 28124) if get_divisors_sum(i) > i)
abundant_sums = set(a + b for a, b in itertools.product(abundant, abundant))
not_possible = set(xrange(1, 28124)) - abundant_sums

print sum(not_possible)
