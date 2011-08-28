#!/usr/bin/env python3

def main():
    number = 20
    while True:
        if isEvenlyDivisible(number):
            print(number)
            return
        number = number + 20

def isEvenlyDivisible(number):
    for x in range(1, 20):
        if number % x != 0:
            return False
    return True

if __name__ == '__main__':
    main()
