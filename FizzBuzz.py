import sys


file = open(sys.argv[1], 'r').readlines()
lines = [line.rstrip() for line in file]



line_lst = []

for line in lines:
    line_lst.append(line.split())



def fb(n, x, y):
    res = []
    for i in range(1,n + 1):
        if i % x == 0 and i % y == 0:
            res.append('FB')
        elif i % x == 0 and not i % y == 0:
            res.append('F')
        elif i % y == 0 and not i % x == 0:
            res.append('B')
        else:
            res.append(i)
    return res

for line in line_lst:
    result = []
    result = fb(int(line[2]), int(line[0]),int(line[1]))
    print ' '.join(str(v) for v in result).strip()
