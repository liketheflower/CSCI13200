def get_max_profit(goods, c):
    profits = [good[1] for good in goods]
    weights = [good[0] for good in goods]
    if sum(weights) <= c: return sum(profits)
    goods.sort(key = lambda x:x[1]/x[0], reverse=True)
    res = 0
    choices = []
    for good in goods:
        w, p = good
        if c-w<=0:
            choices.append((p, c))
            res += c*(p/w)
            break
        else:
            choices.append((p, w))
            res += p
            c -= w
    print(choices)
    return res
goods = [[2, 10], [3, 5],[5, 15], [7, 7], [1, 6], [4, 18], [1, 3]]
print(get_max_profit(goods, 15))
