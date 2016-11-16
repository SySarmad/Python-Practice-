"""
Created By Sarmad Syed 11/7/2016
RansomNote: sees if it is possible to create a ransom
note from a magazine
"""
from collections import defaultdict

def canConstruct(ransomNote, magazine):
    """ @:canConstruct: takes in two strings and returns a true value
        if one string can be constructed from the other
        @:param ransomNote: is the note to be written
        @:param magazine: the string the note should be constructable from
    """
    if ransomNote and magazine is None or ransomNote == magazine:
        return True

    mag_count = defaultdict()
    ran_count = defaultdict()
    for c in magazine:
        if c in mag_count:
            mag_count[c] = mag_count.get(c) + 1
        else:
            mag_count[c] = 1
    for c in ransomNote:
        if c in ran_count:
            ran_count[c] = ran_count.get(c) + 1
        else:
            ran_count[c] = 1
    res = []
    for k, v in zip(ran_count.keys(), mag_count.keys()):
        if k in mag_count.keys() and ran_count.get(k) <= mag_count.get(k):
            res.append(True)
    if len(res) == len(ran_count.keys()):
        return True
    else:
        return False


print canConstruct('aaa', 'aaab') #true
print canConstruct('aa', 'aaaaa') #true
print canConstruct('cc', 'dd') #false
print canConstruct('tassss', 'ssssttta') #true
print canConstruct(' ', ' ') #true
print canConstruct('cc', 'd') #false
print canConstruct('c', 'cd') #true
print canConstruct('cc', 'ddc') #false
print canConstruct('ddddd', ' d') #false
