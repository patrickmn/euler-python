#!/usr/bin/env python3
n = 100
result = 100
while n > 0:
     result = result * n
     n = n - 1
print(sum(int(x) for x in str(result)))
