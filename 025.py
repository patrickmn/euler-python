#!/usr/bin/env python3
a, b = 0, 1
count = 1
while True:
    if len(str(b)) == 1000:
        print(count)
        break
    a, b = b, a + b
    count = count + 1
