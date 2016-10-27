"""
Created by Sarmad Syed 10/15/2016
StringMatch: checks if one string is
the substring of another in O(n)
"""
import sys
import re

""""
@pattern_checker : takes a string as a paramter
and checks it for regex * characters in succession
"""


def pattern_checker(pattern):
    if len(pattern) == 1 and pattern == '*':
        return True
    for i in range(len(pattern)):
        if pattern[i] == ' ' and pattern[i+1] == '*':
            return True
        return False

"""
@string_matcher : takes in two strings, creates
a regex pattern and evaluates if one
string is a substring of the other.
"""


def string_matcher(search, pattern):
    if pattern_checker(pattern):
        return 'false'
    pattern_re = re.compile(pattern, )
    if re.findall(pattern_re, search):
        return 'true'
    return 'false'

""""
opens file with test lines and passes it to methods
"""
with open(sys.argv[1], 'r') as file:
    for lines in file:
        a, b = lines.strip().split(',')

        print "".join(string_matcher(a, b)) + ' ' + a + ' ' + b
