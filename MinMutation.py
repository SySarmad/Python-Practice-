"""
Created by Sarmad Syed 10/20/2016
MinMutation: is a program to count how many
mutations two genes would take to be identical
O(n) time
"""

"""
@min_mutation takes in a start string, and an end
string, and a list of strings called the bank
counts how many mutations it would take the start
string to become identical to the end string
"""


def minMutation(start, end, bank ):
        count = 0         # @count to hold number of occurrences initialized at 0

        # checks either string is empty or mismatched in size, and checks if end is in bank
        if (len(start) != len(end)) or (len(start) == 0 or len(end)== 0) or end not in bank:
            return -1
        # iterate through both strings and checks if letters are equal -> increment count by 1
        for i in range(len(start)):
            if start[i] != end[i]:
                count += 1
        return count

# Test strings and banks
e = "AACCGGTA"
s = "AACCGGTT"
bank = ["AACCGGTA"]
s2 = "AACCGGTT"
e2 = "AAACGGTA"
bank2 = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

print minMutation(s,e,bank)
print minMutation(s2, e2, bank2)

# end of test statments
