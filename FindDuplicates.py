"""
Created by Sarmad Syed 10/30/2016
FindDuplicates: Takes in an array of integers
and outputs the duplicates that appear in
the array
"""
from itertools import *

def findDuplicatesinSorted(a):
    """Takes in a list of ints in sorted order and returns list of ints of duplicates"""
    res = []
    if len(a) <= 1:
        return a
    for i, c in enumerate(a):
        if i < len(a)-1 and c ^ a[i+1] == 0:
            res.append(c)
    set_res = set(res)
    return [x for x in set_res]

def findIndexofDuplicatesSorted(a):
    """Takes in a list of ints in sorted order and returns the first
       index of all the duplicates in the list
    """
    res = []
    if len(a) <= 1 and a[0]==a[1]:
        return [0]
    for i, c in enumerate(a):
        if i > 0 and i < len(a)-1 and c ^ a[i + 1] == 0:
            res.append(i)
    return res


def findDuplicates(a):
    """Takes in a list of ints in unsorted order and returns a list of ints of duplicates"""
    if len(a) <= 1:
        return a
    seen = set()
    seen_add = seen.add
    seen_twice = [x for x in a if x in seen or seen_add(x)]

    return seen_twice

def findDuplicatesIndex(a):
    """Takes in a list of ints in unsorted order and returns
        a list of indices of the Second occurrence of duplicate
    """
    if len(a) <= 1 and a[0] == a[1]:
        return [0]
    seen = set()
    seen_add = seen.add
    res = []
    for i, c in enumerate(a):
        if c in seen or seen_add(c):
            res.append(i)


print findDuplicatesinSorted([1,2,2,3,4,5,6,7,7,8,9,9,9,10,11,12])
print findDuplicatesinSorted([12,11,11,10,9,8,7,7,6,5,4,3,3,2,1])
print findIndexofDuplicatesSorted([12,11,11,10,9,8,7,7,6,5,4,3,3,2,1])

print findDuplicates([1,2,3,4,2,7,5,3,4,7,8])
print findDuplicatesIndex([1,2,3,4,2,7,5,3,4,7,8])