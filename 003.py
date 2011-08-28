#!/usr/bin/env python3

def prime_factors(n):
    factors = []
    lastresult = n
    c = 2
    while lastresult != 1:
        if lastresult % c == 0 and c % 2 > 0:
            factors.append(c)
            lastresult /= c
            c = c + 1
        else:
            c = c + 1
    return factors

# print prime_factors(13195)
print(max(prime_factors(600851475143)))
