#!/usr/bin/env python3

def main():
    sum = 0
    sum_squares = 0
    for x in range (1, 101):
        sum = sum + x
        sum_squares = sum_squares + (x * x)
    square_sum = sum * sum
    difference = square_sum - sum_squares
    print(difference)

if __name__ == '__main__':
    main()
