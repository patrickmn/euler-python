#!/usr/bin/env python3

def main():
    results = []
    for x in range(100, 1000):
        for y in range(100, 1000):
            product = x * y
            if isPalindrome(product):
                results.append(product)
    print(max(results))

def isPalindrome(number):
    word = str(number)
    reverse = word[::-1]
    if word == reverse:
        return True

if __name__ == '__main__':
    main()
