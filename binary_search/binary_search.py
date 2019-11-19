target = 670
def binary_search(target):
    l, r = 0, 1000
    while l<r:
        #m = l+ (r-l)//2
        m = (l+r)//2
        if m == target:return m
        elif m<target:
            l = m+1
        elif m>target:
            r = m-1
    return l

print(binary_search(target))
