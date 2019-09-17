"""
Due the following class and we will talk the solution at the beginning of the following class.
Please ONLY submit it to black board. 

1. write a function to get the sum of 1 to n(inclusively) by using a list.
"""
def get_sum_from_1_to_n(n):
    res = []
    for i in range(1, n+1):
        res.append(i)
    print(res)
    return sum(res)
n = 10
res = get_sum_from_1_to_n(n)
print('res is sum from 1 to n is ', n,  res)
"""
2. 1) create a list named a contains numbers: 10,9,8,... 1.
   2) print the first element of this list.
   3) print the first 3 elements of this list.
   4) print the last element of this list.
   5) get a reverse version of this list.
   6) what is the output of a new list c = a+a
"""
a = []
for i in range(10, 0, -1):
    a.append(i)
print(a)
print('first element', a[0])
print('first 3 element', a[0:3])
print('last element', a[-1])
print('reverse of a', a[::-1])
c = a + a
print('c:a+a', c)


"""
  
  
  7) execute the follwing program to see what will happen:

while len(a)>0:
    this_element = a.pop()
    print('length of list a', len(a))
    print('a', a) 
    print('this_element', this_element)

"""
b = a[:]
print('b', b)
while len(a)>0:
    this_element = a.pop()
    print('length of list a', len(a))
    print('a', a) 
    print('this_element', this_element)

while b:
    this_element = b.pop()
    print('length of list b', len(b))
    print('b', b) 
    print('this_element', this_element)
