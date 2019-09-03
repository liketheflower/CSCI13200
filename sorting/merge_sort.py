"""
This code is used to implement merge sort
"""
import collections
def merge_sort(a):
    if len(a)<=1:return a
    N = len(a)
    left, right = merge_sort(a[:N//2]), merge_sort(a[N//2:])
    left, right = collections.deque(left), collections.deque(right)
    res = []
    print(left, right)
    if left and right:
        l, r = left.popleft(), right.popleft()
    else:
        return list(left)+list(right)
    while True:
        if l<r:
            res.append(l)
            if left:
              l = left.popleft()
            else:
              return res+[r]+list(right)
        else:
            res.append(r)
            if right:
              r = right.popleft()
            else:
              return res+[l]+list(left)
a=[3,4,1]
print(merge_sort(a))



