#!/usr/bin/env python3

a, b = 0, 1
total = 0
while b < 4000000:
    if b % 2 == 0:
        total = total + b
    a, b = b, a + b
print(total)
