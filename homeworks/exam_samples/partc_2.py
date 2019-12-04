names = "alex,jimmy,susan,sophia,Andrew"
IDs = "1,2,5,2,4"
performance = "A+,A,A,A-,INC"
def performance_hack(performance):
    old_performance_new_performance = {'A+':'A+',
                                       'A':'A+',
                                       'A-':'A',
                                       'INC':'A-'}
    performance_list = performance.split(',')
    performance_new = [old_performance_new_performance[old_performance] for old_performance in performance_list]
    return ','.join(performance_new)

print('original performance: ', performance)
performance =  performance_hack(performance)
print('new performance: ', performance)

def find_duplication(a):
    return len(set(a)) == len(a)

if find_duplication(IDs.split(',')):
    print('Hello, professor, there is no duplication in the ID list.')
else:
    print('Hello, professor, there ARE some duplications in the ID list.')
