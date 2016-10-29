"""
Created by Sarmad Syed 10/27/2016
StringBeauty: Finds the maximum sum
of char in the array
"""

import sys
from collections import Counter as count
import string

def beauty_strings(s):
   res = 0
   out = s.translate(string.maketrans("", ""), string.punctuation)
   c = count(out.replace(" ",""))
   a = c.most_common(26)
   keys = []
   values = reversed(range(1,27))
   for i in a:
       keys.append(i[0])
   dct = dict(zip(keys,values))
   for c in s:
       res += dct.get(c,0)
   return res

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if len(test) == 0:
            print 0
        print beauty_strings(test.lower().strip())
