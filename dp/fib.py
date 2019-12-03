from functools import lru_cache
@lru_cache(None)
def fib_top_down(n):
    if n==0: return 0
    if n==1: return 1
    return fib_top_down(n-1)+fib_top_down(n-2)

def fib_bottom_up(n):
    if n==0: return 0
    if n==1: return 1
    a, b = 0, 1
    for i in range(2, n+1):
        c = a + b
        a, b = b, c
    return c
def fib_bottom_up2(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

for n in range(1, 10):
    print(fib_top_down(n))
    print(fib_bottom_up(n))
    print(fib_bottom_up2(n))
