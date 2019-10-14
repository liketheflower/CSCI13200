"""
This project is realted to how to use sort algorithms.
It has several parts described below:
1. Random list generation.
2. Sort different random lists by using different algorithms.
3. Compare the performance of different sorting algorithms.

The random list generation function is provided here.
"""
import random
def get_n_random_numbers(n):
    """
    generate a list contain n random numbers. random.random() will generate random number between 0 to 1. Hence, 1000*random.random() will generate random number between 0 to 1000.
    """
    random.seed(0)
    return [1000*random.random() for _ in range(n)]
# test the random number generator
print(get_n_random_numbers(10))
long_random_list = get_n_random_numbers(100)
import matplotlib.pyplot as plt
plt.scatter(list(range(len(long_random_list))), long_random_list, c ='#f46d43', alpha=0.8,s=10, label='before sort')
plt.scatter(list(range(len(long_random_list))), sorted(long_random_list), c ='#66bd63', alpha=0.4,s=10, label='after sort')
plt.legend(loc='upper center')
plt.show()
"""
You are suppose to do:
1. implement your own two sorting algorithms (insertation sort, quick sort or merge sort)
2. generate random lists with length of [10, 100, 1000, 10000, 1000000], and use your two sorting algorithms to sort the random list.
3. When the length of the list is 1000, visualize the list befor sorting and after sorting to check the correctness of your algorithm.
4. Use the system built in sort algorithm to repeat step 2.
5. Timing these sorting THREE algorithms (two your own and one system built in) and plotting your results to make a comparison. 

"""
# Timing code
import time
def fibonacci_numbers(n):
    if n==0:return 0
    elif n==1:return 1
    else:return fibonacci_numbers(n-1)+fibonacci_numbers(n-2)

memo = {}
def fibonacci_numbers_with_memo(n):
    if n not in memo:
        if n==0:memo[n] = 0
        elif n==1:memo[n] = 1
        else: memo[n] = fibonacci_numbers_with_memo(n-1)+fibonacci_numbers_with_memo(n-2)
    return memo[n]
n = 32
begin_time = time.time()
print('fibonacci_numbers ', n, 'is:', fibonacci_numbers(n))
end_time = time.time()
print('without memo, execution time of fibonacci_numbers ',n ,' is ', end_time-begin_time)

begin_time = time.time()
print('fibonacci_numbers ', n ,' is:', fibonacci_numbers_with_memo(n))
end_time = time.time()
print('with memo, execution time of fibonacci_numbers ' ,n, 'is ', end_time-begin_time)
