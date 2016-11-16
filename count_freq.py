"""
Created by Sarmad Syed 11/9/16
count_freq: sorts a string based on
frequency of characters in descending order
case is considered
"""
from collections import Counter

def freq_sort(s):
    if s is None or s == " ":
        return s
    count = Counter(s)
    return ''.join(e[0] * e[1] for e in count.most_common(len(s)))

def longestPalindromeSubstring(s):
        if len(s) > 1000:
            return None
        if s is None or s == " " or len(set(s)) == 1:
            return s
        r = ""
        i = 1
        j = len(s) - 1
        while i < j:
            print s[i:] +"   "+ s[::-i]
            i += 1
            j -= 1
print longestPalindromeSubstring('asdasdhannah')

