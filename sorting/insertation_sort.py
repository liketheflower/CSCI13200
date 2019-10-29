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


def insertation_sort_bottom_up(a):
    if len(a)<=1: return a
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j]<a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            else:break
    return a
a = [1, 2, 3, 1, 0, -1, 99, -199]

import random
def get_n_random_numbers(n):
    """
    generate a list contain n random numbers. random.random() will generate random number between 0 to 1. Hence, 1000*random.random() will generate random number between 0 to 1000.
    """
    random.seed(0)
    return [1000*random.random() for _ in range(n)]
print(insertation_sort(a))
import time
s = time.time()
print(insertation_sort_bottom_up(a))          
c = get_n_random_numbers(10000)
d = insertation_sort_bottom_up(c[:])
import matplotlib.pyplot as plt
plt.scatter(range(len(c)), c, alpha = 0.3, c= '#ff0000')
plt.scatter(range(len(d)), d, alpha= 0.01, c = '#0000ff')
plt.show()
e = time.time()
print(e-s)
