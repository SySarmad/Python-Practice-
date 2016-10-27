import sys

f = open(sys.argv[1]).readlines()

str_lst = list([str(v).strip() for v in f])


result = []


def str_check(tup):
    a, b = tup
    if a[-len(b):] == b:
        return 1
    return 0


for elem in str_lst:
    tup = ()
    tup = elem.split(',')
    print str_check(tup)

