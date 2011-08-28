#!/usr/bin/env python3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
f = open('022-names.txt', 'r')
names = sorted(f.read().replace('"', '').split(','))
total = 0
idx = 1
for name in names:
    total = total + (idx * sum(alphabet.index(x.lower()) + 1 for x in name))
    idx = idx + 1
print(total)
