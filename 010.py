#!/usr/bin/env python3

# The Sieve of Eratosthenes
primes = [2,]

def main():
    number = 3
    while number < 2000000:
        if isPrime(number):
            primes.append(number)
        number = number + 2
    print(sum(primes))

def isPrime(number):
    for x in primes:
        if number % x == 0:
            return False
    return True

if __name__ == '__main__':
    main()
