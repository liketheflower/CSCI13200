# jimmy shen
# Oct 11, 2019

def quick_sort(a):
    # base case:
    if len(a)<=1:return a
    mid = a[0]
    rest = a[1:]
    left = [element for element in rest
                    if element < mid]
    right = [element for element in rest
                    if element >= mid]
    #return left part + middle + right part
    return quick_sort(left) + [mid] + quick_sort(right)

a = [1, -2, -3, 4, -100,10]
print(quick_sort(a))
print(sorted(a))
