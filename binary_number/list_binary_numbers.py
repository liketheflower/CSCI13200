def get_binary_numbers(n):
    if n==1: return ['0', '1']
    if n==2: return ['00', '01', '10', '11']
    #if n==3: return (['0'+'00', '0'+'01','0'+ '10','0'+ '11']+
    #                 ['1'+'00', '1'+'01','1'+ '10','1'+ '11'])
    #if n==3: return [first+rest for first in ['0', '1']
    #                            for rest in get_binary_numbers(n-1)]
    return [first+rest for first in ['0', '1']
                                for rest in get_binary_numbers(n-1)]
print(get_binary_numbers(1))
print(get_binary_numbers(2))
print(get_binary_numbers(3))
print(get_binary_numbers(4))
#print(get_binary_numbers(10))
                
