"""
Due the following class and we will talk the solution at the beginning of the following class.
Please ONLY submit it to black board. 

1. Print 1 to 10 '*' and get output like this(hint: 'a*4 will be 'aaaa', simlar '*'*4 will be '****'. 
if you want to output 4 '*', pls use this code "print('*'*4)'":
*
**
***
...
**********
"""
# SOLUTION
def print_start_from_1_to_n(n):
    """
    this function will print 1 '*' to '*'*n 
    Args:
    n: integer number indicates how mnay star will be printed in the last row

    Returns:
    None
    """
    for i in range(1, n+1):
        print('*'*i)
print_start_from_1_to_n(10)
print_start_from_1_to_n(1)
"""
2. Print 10 to 1 '*' and get output like this:
**********
*********
...
*

"""
def print_start_from_n_to_1(n):
    for i in range(n, 0, -1):
        print('*'*i)
print_start_from_n_to_1(10)
"""
3. write a function to output 1 to n '*'.

4. write a function to output 1 to n '*' and then n-1 '*' to 1 '*'.
"""
def print_start_from_1_to_n_back_to_1(n):
    print_start_from_1_to_n(n)
    print_start_from_n_to_1(n-1)
    """
    for i in range(1, n+1):
        print('*'*i)
    for i in range(n-1, 0, -1):
        print('*'*i)
    """
print_start_from_1_to_n_back_to_1(9)

"""
5. write a function to get the sum of 1 to n(inclusively)
"""
def get_sum_from_1_to_n(n):
    sums = 0
    for i in range(1, n+1):
        print('i:', i,'old sums:', sums)
        sums = sums + i
        print('i:', i,'new_sums:', sums)
    return sums
n = 100
sums = get_sum_from_1_to_n(n)
print('sum from 1 to',n ,' is:', sums)
print('another way to solve this problem')

sums = sum(list(range(1,n+1)))
print('sum from 1 to',n ,' is:', sums)

    

