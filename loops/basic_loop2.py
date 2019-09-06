"""
Basic loops: continue, break
jimmy shen
Sep 6, 2019
"""
print('what the continue is doing')
for i in range(20):
    if i==9:
        continue
    print('hello world', i)
print('what the break is doing')
for i in range(20):
    if i==9:
        break
    print('hello world', i)
