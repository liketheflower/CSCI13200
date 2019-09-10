# print hello world from hello world 0 to hello workd 10
# print hello world from hello world 0 to hello workd 17
# print hello world from hello world 0 to hello workd 29



"""
for i in range(11):
    print('hello world ', i)

for i in range(18):
    print('hello world ', i)

for i in range(30):
    print('hello world ', i)


"""
def print_something():
    for i in range(10):
        print('I love python')

def print_helloworld_n_times(n):
    for i in range(n):
        print('hello world ', i)
def print_something_n_times(something, n):
    for i in range(n):
        print(something, i)
m = 11
print_helloworld_n_times(m)
print_helloworld_n_times(18)
print_helloworld_n_times(30)
print_something()
print_something_n_times('I hate programming', 10)
