from itertools import product
def get_n_bits_number(n):
    a_list = [['0','1'] for _ in range(n)]
    res = list(product(*a_list))
    print(len(res))
get_n_bits_number(2)
get_n_bits_number(3)
get_n_bits_number(8)
