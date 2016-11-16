"""Created by Sarmad Syed 11/07/2016:
TargetinRotated: practice with rotated lists
and using generators and lambda functions
"""
import timeit

def maxRotateFunction(a):
    if a is None or len(a) == 0:
        return 0
    sums = 0
    for i, c in enumerate(sorted(a)):
        sums += i * c
    return sums
print maxRotateFunction([4,3,2,6])
