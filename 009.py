#!/usr/bin/env python3

def main():
    a = 1
    b = 2
    c = 3
    while c < 1000:
        a2 = 0
        b2 = 0
        c2 = 0
        if checkTriplet(a, b, c):
            return
        else:
            b2 = b + 1
            while b2 < 1000:
                if checkTriplet(a, b2, c):
                    return
                c2 = c + 1
                while c2 < 1000:
                    if checkTriplet(a, b2, c2):
                        return
                    c2 = c2 + 1
                b2 = b2 + 1
        a = a + 1
        b = b + 1
        c = c + 1

def checkTriplet(a, b, c):
    if (a * a) + (b * b) == (c * c) and a + b + c == 1000:
        print("a: {0}, b: {1}, c: {2}, sum: {3}, product: {4}".format(a, b, c, (a + b + c), (a * b * c)))
        return True

if __name__ == '__main__':
    main()
