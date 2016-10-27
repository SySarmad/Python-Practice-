"""
Created by Sarmad Syed 10/4/2016
Anagram Checker: on method is Anagram,
checks if two words are annagrams of each other
works in O(n) time
"""

"""
@is_anagram takes in two parameters s and t, both strings
and checks if they are anagrams of each other
"""


def is_anagram(s, t):
        if len(s) != len(t):                      # Checks length of strings if not equal return False
            return False
        counter_string = {}                   # @counter_string = dictionary for holding key, value of chars and freq

        for char in s:                        # iterates through string and adds keys and values to counter_string
            if char not in counter_string.keys():
                counter_string[char] = 0
            counter_string[char] = counter_string.get(char) + 1

        for char in t:               # iterates through target string and checks if key exists, decrements value by 1
            if char in counter_string.keys():
                counter_string[char] = counter_string.get(char) - 1
                if counter_string[char] == 0:       # if value for the key is equal to zero remove the key
                    counter_string.pop(char,0)

        if len(counter_string) == 0:        # if all keys and values are gone return True else return False
            return True
        return False

print is_anagram("aaaaabbb","aaaabbbb")   # tests function with two strings