"""
basic list operations
Sep 13, 2019
jimmy shen
"""
# sum of 1 to n by using list
def sum_1_to_n(n):
    a = []
    for i in range(1, n+1):
        a.append(i)
    print(a)
    return sum(a)
n = 100
res = sum_1_to_n(n)
print(res)


a = [1, 2, 3, 4, 5]
b = [10, 13, -1, -1000]

print('a', a)
print(a[0])
print(a[-1])
print('length of list a', len(a))
c = a+b

print('b', b)
print('c is a+b, what is c', c)
c = c[::-1]
print('reserve c', c)
