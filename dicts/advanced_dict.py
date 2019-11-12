import collections
a = ['a', 'aa', 'ab','cd','a', 'abc']
cnt = collections.Counter(a)
print(cnt)
my_cnt = collections.defaultdict(int)
for item in a:
    my_cnt[item] += 1
print(my_cnt)
my_cnt_list = collections.defaultdict(list)
for item in a:
    my_cnt_list[len(item)].append(item)
print(my_cnt_list)
two_layer_dict = collections.defaultdict(lambda :collections.defaultdict(list))
for item in a:
    two_layer_dict[len(item)][item[0]].append(item)
print(two_layer_dict)
