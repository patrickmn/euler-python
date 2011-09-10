#!/usr/bin/python3
sum = 0
for x in range(1, 1001):
    sum += x**x
str = str(sum)
print(str[len(str)-10:])
