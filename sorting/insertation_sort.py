# Oct 7, 2019
# jimmy shen
# Implement the insertation sort algorithm.

def insertation_sort(a):
    if len(a)<=1: return a
    sorted_a = insertation_sort(a[:-1])+[a[-1]]
    for i in range(len(a)-2, -1, -1):
        if sorted_a[i+1] < sorted_a[i]:
            sorted_a[i], sorted_a[i+1] = sorted_a[i+1], sorted_a[i]
        else:
            break
    return sorted_a


a = [1, 2, 3, 1, 0, -1, 99, -199]
print(insertation_sort(a))
          
