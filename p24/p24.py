import math

def nth_permutation(input_vals, n):
    # we are going to be popping values out
    input_vals = list(input_vals)

    # nth permutation is the (n-1)st change of order
    n -= 1

    output = []

    #place values from most options left to least
    for place_val in reversed(xrange(len(input_vals))):
        # for a list size of 10, each change of top level digit
        # is 9! permutations, and so forth for each position
        num_levels = n // math.factorial(place_val)

        # if we have sufficient room for 2 of that factorial, skip over 2 of the input vals in order
        output.append(inputs.pop(num_levels))

        # see how many permutations are left after the largest amount are removed
        n -= (math.factorial(place_val) * num_levels)

    return output

inputs = [ str(c) for c in xrange(10) ]
print ''.join(nth_permutation(inputs, 1000000))
