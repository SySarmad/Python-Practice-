"""
Created by Sarmad Syed 11/12/2016
Out_think: a variation of fizz buzz
given three integers n, p, q
n bieng the range, if a number is divisible
by p or q print out, if it is equal to either
digit of the decimal representation either p
or q, print out think if both
"""
import sys


def checkInteger(num, p, q):
    if num % p == 0 and num % q == 0:
        return True
    else:
        return False


def checkDecimal(num, p, q):
    dec = float(num)
    a, b = str(dec).split('.')
    if int(a) % p == 0 and int(b) % q == 0:
        return True
    else:
        return False


def out_think(s):
    string = s.split(",")
    n, p, q = (int(i) for i in string)
    for i in range(1, n+1):
        if checkDecimal(i, p, q) and checkInteger(i, p, q):
            yield 'OUT-THINK'
        elif checkDecimal(i, p, q) and not checkInteger(i, p, q):
            yield 'THINK'
        elif checkInteger(i, p, q) and not checkDecimal(i, p, q):
            yield 'OUT'
        else:
            yield i

with open(sys.argv[1]) as file:
    for line in file:
        print [i for i in out_think(line)]