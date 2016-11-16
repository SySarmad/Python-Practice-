"""
Created by Sarmad Syed 10/25/2016
LetterCombNum: is a program that
finds all the possible letter telephonic combinations
from a string of numbers in the correct phone order
emulates telephone string operations
"""

def perm_maker(dct, digits):
   res = ''
   





def letterCombinations(s):
    """
    @:param letterCombinations takes in a string s
    and passes a dictionary and list of keys constructed
    from the string
    """
    if s is None:
        return 0

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
        '#': ['']
    }

    if len(s) == 1:
        return "".join(e for e in number_dict.get(s))
    digis = [int(i) for i in s]
    return perm_maker(number_dict, digis)




print letterCombinations('23')
print letterCombinations('2')
print letterCombinations('234')