"""
Created by Sarmad Syed 10/25/2016
Macbeth.py : A Program that takes in texts, and counts
the words in O(n) time
"""
import sys
import string as s
from collections import Counter
"""
Import sys for arguments,
import string for translation(remove punctuations)
import Counter from collections library
"""
input_string = ""                                        # @input_string: creates raw string to be processed from text

with open(sys.argv[1]) as file:                             # Opens argument as file
    for line in file:                                        # Iterate through file
        if not line.isspace():                                 # Check if line is space
            input_string += " " + line.strip().lower()           # strip, lower, and concat each line to input_string

# @translation: creates new string from input_string with all occurrences of ",.?:;!" removed
translation = input_string.\
    translate(s.maketrans("", ""), s.punctuation)

res = Counter()                                            # @res: Creates counter object

"""
Iterate through processed string and check for words with
length greater than 4 and add them to Counter
"""
for word in translation.split():
    if len(word) > 4:
        res[word] += 1

sol = res.most_common(2)                           # @sol: creates a list of two most common words from dictionary

# Print the second most common word and number of occurrences.
print "The second most repeated word is 5 char or more: '" + \
      str(sol[1][0]) + "' and it appeared: " + str(sol[1][1]) + " times"
