"""
Created by Sarmad Syed 10/27/2016
ReverseWords: Reverses the words
in an input string
"""

import sys

def _reverse_words(s):
    sol = ""
    for word in reversed(s.split()):
        sol += word + " "
    return sol


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print _reverse_words(test)
