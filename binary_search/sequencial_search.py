target = 670
def seq_search(target):
    for i in range(1, 1000+1):
        if i==target:
            return i

print(seq_search(target))
