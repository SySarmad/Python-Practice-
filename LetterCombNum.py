"""
Created by Sarmad Syed 10/25/2016
LetterCombNum: is a program that
finds all the possible letter telephonic combinations
from a string of numbers in the correct phone order
emulates telephone string operations
"""

"""
@def letterCombinations takes in one parameter s
creates a dictionary of numbers as they appear on a
keypad 2-9 as keys and a list of values those digits represent
as the value
"""
def letterCombinations(s):
    if len(s) == 0:
        return []
    number_dict = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r','s'],
        '8': ['t', 'u', 'v'],
        '9': ['w','x','y','z'],
        '0': [' '],
        '*': ['+'],
        '#': ['']}
    if len(s) == 1:
        return number_dict.get(s)
    string = []
    for c in s:
        string.append(c)





print letterCombinations('23')
print letterCombinations('2')
print letterCombinations('234')