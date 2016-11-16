"""
Created by Sarmad Syed 10/29/2016
JollyJumpers: Checks if the values in
the array are the absolute value differences
of the values in the array
"""

import sys       # Imports the system

def jolly_jumper(arry):
    s = [int(s) for s in arry]
    bools = []
    for i in s:
        


with open(sys.argv[1]) as file:
    for test in file:
        digis = test.split()
        print jolly_jumper(digis)