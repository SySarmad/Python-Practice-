"""
Created by Sarmad Syed 10/22/2016
LongestParen: program to check if
a string of parenthesis is valid
"""

"""
@longest_valid_parenthesis takes in a
string, and uses a stack to check if
parenthesis is valid and returns the
number of valid parenthesis.
"""


def longestValidParenthesis(s):
    if len(s) <= 1:
        return -1
    res = []
    count = 0
    for i, c in enumerate(s):
        if c == '(':
            res.append(i)
        else:
            if c == ')':
                if s[res.pop()] == '(':
                    continue

    return res


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        depth = 0
        if root is None:
            return depth
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1



