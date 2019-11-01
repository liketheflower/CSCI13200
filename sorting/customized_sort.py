def my_add(a, b):
    return a+b
def my_add_new(func, a,b):
    return func(a, b)
print(my_add_new(my_add, 2,3))

a = [1, -2, 9, -10]
def identity(x):return x
def my_reverse(x):return -x
print(sorted(a))
print(sorted(a, key=my_reverse))
print(sorted(a, key=lambda x:-x))

