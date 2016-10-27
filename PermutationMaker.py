
def perm_maker(string):
    res = [''.join(p) for p in permutations(string)]
    res_sorted = sorted(res, key=lambda x :[0])
    print ' '.join(str(v) for v in res)

with open(sys.argv[1]) as f:
    str_lst = list([str(v).strip() for v in f])

for string in str_lst:
    perm_maker(string)

