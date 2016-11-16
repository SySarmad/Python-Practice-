"""
Created by Sarmad Syed 11/1/2016
FindSingles: find values that appear once
in an array of duplicates
"""
from collections import Counter
def findSingleValue(a):
    """Takes in a list of ints and finds the elements that only
        appear once
        :param a: a list of ints
        :return res: a list of ints
    """
    res = 0
    if len(a) <= 1 and a[0] == a[1]:
        return a
    for i in a:
        res ^= i
    return res


def findIntersection(a, b):
    if len(a) == 0 or len(b) == 0:
        return -1
    res = set(i for i in a if i in b)
    return [i for i in res]


def canConstruct(s, m):
    if s == m:
        return True
    if len(s) == 0 or len(m) == 0 or len(s) > len(m):
        return False
    d = Counter(s)
    g = Counter(m)
    res = []
    for k in d.keys():
        if d.get(k) == g.get(k):
            res.append(True)

    if len(res) == len(d.keys()):
        return True
    return False


def findLetter(s, t):
    if len(s) == 0:
        return -1
    sol = sum(ord(c) for c in s)
    res = sum(ord(c) for c in t)
    return chr(abs(sol - res))


print findLetter('abcd', 'abcde')

print findSingleValue([1,1,2,2,4,3,4,5,5,6,6,7,7,8,8])
print findIntersection([1,2,2,1], [2,2])

print canConstruct('a', 'b')
print canConstruct('aab', 'aba')
print canConstruct('cando', 'codan')
print canConstruct('aa', 'aab')
print canConstruct('','')