#!/usr/bin/env python3

# The Sieve of Eratosthenes
primes = []

def main():
    number = 2
    while len(primes) < 10001:
        if isPrime(number):
            primes.append(number)
        number = number + 1
    print(primes[10000])

def isPrime(number):
    for x in primes:
        if number % x == 0:
            return False
    return True

if __name__ == '__main__':
    main()
