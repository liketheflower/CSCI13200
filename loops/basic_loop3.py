"""
Basic loops
jimmy shen
Sep 6, 2019
"""
i = 0
while i<10:
    i = i+1
    if i==8:
        continue
    print('hello world!', i)

i = 0
while True:
    i = i+1
    if i==9:
        break
    print('hello world!', i)
