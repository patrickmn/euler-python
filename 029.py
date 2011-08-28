#!/usr/bin/env python3
nums = set()
a = 2
while a <= 100:
    b = 2
    while b <= 100:
        nums.add(a**b)
        b += 1
    a += 1
print(len(nums))
