a = []
for i in range(10):
    a.append(i)
print(a)

# list comprehension
a = [i for i in range(10)]
print(a)


a= [-10, 9, 7, 9, 19,1000]
# traverse a list
for element in a:
    print(element)
print('another way to traverse a list')
for i in range(len(a)):
    print(a[i])

print('a third way to traverse a list')
for i, element in enumerate(a):
    print(i, element)

print('length of list a', len(a))
print('sum of list a', sum(a))
print('maximum value of list a', max(a))
print('minimum value of list a', min(a))

print('index of maximum value of list a', a.index(max(a)))
print('index of minimum value of list a', a.index(min(a)))

