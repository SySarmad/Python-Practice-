from stack import Stack

def is_valid(s):
    if s is None or s == " ":
        return False
    stk = Stack()
    for c in s:
        if c == '{' or c == '[' or c == '(':
            stk.push(c)
        elif c == ')' and stk.peek() == '(':
            stk.pop()
        elif c == ']' and stk.peek() == '[':
            stk.pop()
        elif c == '}' and stk.peek() == '{':
            stk.pop()

    if stk.is_empty():
        return True

    else:
        return False

print is_valid("(())")                              #True
print is_valid("{[()]}")                            #True
print is_valid("[(])")                              #False
print is_valid("((({{{{[[[]]]}}}})))")              #True
print is_valid("(({}))")                            #True
print is_valid("()(){}{}[]((({{{}}})))")            #True