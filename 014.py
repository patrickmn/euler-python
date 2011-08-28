#!/usr/bin/env python3

# Collatz conjecture
import operator

number = 2
seqjump = {}
while number < 1000000:
    seqjump[number] = 0
    n = number
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        seqjump[number] = seqjump[number] + 1
    number = number + 1
largest_set = max(seqjump.items(), key=operator.itemgetter(1))
print("Number producing the largest chain is {0} with {1} jumps.".format(largest_set[0], largest_set[1]))
