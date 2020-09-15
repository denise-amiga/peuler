# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 15:23:53 2020

@author: Denise
"""

from math import gcd


def digitalSum(n):
    return sum(map(int, str(n)))


def triangleGen():
    a, b = 2, 1
    while True:
        yield b, a - 1
        b, a = b + a, a + 1


def fibonacciGen():
    a = b = i = 1
    while True:
        yield a, i
        a, b, i = b, a + b, i + 1


def fibonacciList(l):
    f = [0, 1]
    a, b = 0, 1
    while b < l:
        a, b = b, a + b
        f.append(b)
    return f


def primeFactors(l):
    f = []
    ll = l
    while l % 2 == 0:
        f.append(2)
        l /= 2
    for i in range(3, int(ll ** 0.5) + 1, 2):
        while ll % i == 0:
            f.append(i)
            ll /= i
    return f


def divisors(l):
    d = []
    for i in range(1, int(l ** 0.5) + 1):
        if l % i == 0:
            d.append(i)
            d.append(l // i)
    if i * i == l: d.pop()  # Fix for perfect cuadratric
    #if int(l ** 0.5) * int(l ** 0.5) == l: d.pop()
    return d

def ndivisors(l):
    d = 0
    for i in range(1, int(l ** 0.5) + 1):
        if l % i == 0:
            d += 2
    if i * i == l: d -= 1  # Fix for perfect cuadratric
    #if int(l ** 0.5) * int(l ** 0.5) == l: d -= 1
    return d


def isPalindrome(l):
    txt = str(l)
    lt = len(txt)
    for i in range(lt // 2):
        if txt[i] != txt[lt - i - 1]: return False
    return True


def isPrime(l):
    if l == 2: return True
    if l % 2 == 0: return False
    for i in range(3, int(l ** 0.5) + 1, 2):
        if l % i == 0:
            return False
    return True


def sievePrime(l):
    p = [0] * l
    p[2] = 1
    i = 3
    while i < l:
        p[i] = 1
        i += 2
    i = 3
    while i <= int(l ** 0.5):
        if p[i] == 1:
            j = i * i
            while j <= l:
                p[j] = 0
                j += 2 * i
        i += 2
    return p


def sievePrimeList(l):
    p = sievePrime(l)
    return [x for x, y in enumerate(p) if y == 1]


def lcm(a, b):
    return a * b // gcd(a, b)


def wday(y,m,d):
    a = (14 - m) // 12
    m += 12 * a
    y -= a
    return ((d + (13 * m + 8) // 5 + y + y // 4 - y // 100 + y // 400) % 7)


def num2txt(n):
    n20 = ['zero','one','two','three','four','five','six','seven','eight','nine',
           'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen',
           'seventeen','eighteen','nineteen']
    ndec = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty',
            'ninety']
    if n > 0 and n < 20:
        return n20[n]
    if n > 19 and n < 100:
        if n % 10 == 0: return ndec[n // 10]
        return ndec[n // 10] + str(num2txt(n % 10))
    if n > 99 and n < 1000:
        if n % 100 == 0: return n20[n // 100] + 'hundred'
        return n20[n // 100] + 'hundredand' + str(num2txt(n % 100))
    if n > 999 and n < 10000:
        if n % 1000 == 0: return n20[n // 1000] + 'thousand'
        return n20[n // 1000] + 'thousandand' + str(num2txt(n % 1000))

def cycle(n, l):
    if n % 2 == 0 or n % 5 == 0: return 0
    for i in range(1, l):
        if pow(10, i, n) == 1: return i


def collatzRec(n,i=1):
    #print(n,i)
    if n == 1: return i
    if n % 2 == 0:
        return collatzRec(n // 2, i + 1)
    else:
        return collatzRec(3 * n + 1, i + 1)


def collatz(n):
    r = 1
    while n > 1:
        r += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    return r


def binom(n, m):
     b = [0] * (n + 1)
     b[0] = 1
     for i in range(1, n + 1):
             b[i] = 1
             j = i - 1
             while j > 0:
                     b[j] += b[j-1]
                     j -= 1
     return b[m]

