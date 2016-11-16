"""
Created by Sarmad Syed 11/1/2016
Functional Practice: various technique for functional programming
as well as practice with generators

"""
from operator import add, sub
import re
names = ['Mary', 'Isla', 'Sam']

# generator example
hash_names = (hash(i) for i in names)
# map (functional example)
map_hash_names = map(hash, names)

print [i for i in hash_names], type(hash_names)
print map_hash_names, type(map_hash_names)

print map(hash, names)

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]


func_list = filter(lambda x: 'height' in x, people)
print func_list

def nonfuncAve(d):
    height_total = 0
    height_count = 0
    for person in people:
        if 'height' in person:
            height_total += person['height']
            height_count += 1

    if height_count > 0:
        average_height = height_total / height_count

        return average_height


def recursive_product(x, y):
    if y == 0 or x == 0:
        return 0
    return add(x, recursive_product(x, y-1))


def recursive_divide(x, y):
    if x >= y:
        return recursive_divide(x-y, y) + 1
    return 0

s = [i*i for i in [1,2,3,4,5]]
print type(s)


def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])



def isPalindrome(s):
        if s is None:
            return False
        s = s.replace(" ", "").lower()
        s = re.sub(r'[^\w\s]', '', s)
        out = s.decode('unicode_escape').encode('ascii', 'ignore')

        if out == out[::-1]:
            return True
        else:
            return False


print reverse_string('sarmad')
print isPalindrome('.@hannah@.')
print isPalindrome('OP')


def nest_reverse(s):
    if len(s) == 0:
        return []
    for i, c in enumerate(s):
        print i, c

def reverse_ls(ls):
    if len(ls)== 0:
        return []
    else:
        return [ls[-1]] + reverse_ls(ls[:-1])

mylist = [1, 2, 3, 4, 5]
backwards = lambda l: (backwards (l[1:]) + l[:1] if l else [])
print backwards(mylist)


print reverse_ls([1, 2, 3, 4, 5, 6])

print nest_reverse([1, [2, [3, [4, [5]]]]])


# tests for recursive divide
"""
print recursive_product(4,3)
print recursive_product(5,0)
print recursive_product(0,5)
print recursive_product(12,22)

print recursive_divide(4,3)
print recursive_divide(12,3)
print recursive_divide(4,3)
"""