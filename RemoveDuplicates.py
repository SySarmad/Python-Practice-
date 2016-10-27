from heapq import merge


"""def uniqueify(seq):
    res = set()

    for elem in seq:
        if elem not in res:
            res.add(elem)
            yield elem


for elem in lst:
        result.append(list(uniqueify(elem)))

for elem in result:
    str = ""
    for chr in elem:
        str += chr
    print str
"""



def recursive_merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst)/2

    left = lst[mid:]
    right = lst[:mid]

    left_l = recursive_merge_sort(left)
    right_l= recursive_merge_sort(right)

    return list(merge(left_l, right_l))


lst = [5, 6, 8,4, 3,2,0, 55, 23, 22, 100, 53, 44, 10, 0]

print recursive_merge_sort(lst)


def quick_sort(lst):
    quick_sort_helper(lst, 0, len(lst)-1)

def quick_sort_helper(lst, first, last):
    if last < first:
        split_pnt = partition(lst,first, last)

        quick_sort_helper(lst, first, split_pnt-1)
        quick_sort_helper(lst, split_pnt + 1, last)

def partition(lst, first, last):
    pivot = lst[first]

    left_mark = first + 1
    right_mark = last

    done = False

    while not done:

        while left_mark <= right_mark and lst[left_mark] <= pivot:
            left_mark += 1
        while lst[right_mark] >= pivot and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            temp = lst[first]
            lst[left_mark] = lst[right_mark]
            lst[right_mark] = temp

        