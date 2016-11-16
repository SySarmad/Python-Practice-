"""
Created by Sarmad Syed 11/16/16
Class that defines the ADT Stack, defines
several functions, is_empty, push, peek, pop, size
"""

class Stack:

    def __init__(self):
        """Constructs Stack with an empty list"""
        self.items = []

    def is_empty(self):
        """Returns True if Stack is empty False if is not"""
        return self.items == []

    def push(self, obj):
        """Appends obj to 'top' of the Stack"""
        self.items.append(obj)

    def peek(self):
        """Checks the object at the top of the Stack"""
        return self.items[-1]

    def pop(self):
        """Removes the item from the top of the Stack"""
        return self.items.pop()

    def size(self):
        """Checks and returns the size of the Stack """
        return len(self.items)
