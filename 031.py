#!/usr/bin/env python3
import itertools

coin_units = (
    '100',
    '50',
    '20',
    '5',
    '2',
    '1',
    )

def main():
    count = 0
    for combo in itertools.combinations(coin_units, 3):
        if sum(int(x) for x in combo) == 200:
            count = count + 1
    print(count)

if __name__ == '__main__':
    main()
