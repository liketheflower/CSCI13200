def my_add(a, b):
    return a+b
def my_add_new(func, a,b):
    return func(a, b)
print(my_add_new(my_add, 2,3))
