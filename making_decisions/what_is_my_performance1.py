"""
making decsions
<, > , <=, >= , ==, !=
1<3 and 2>3
input
"""

while True: 
    score = input('Pls input your score of CSCI 13200: ')
    score = int(score)
    if 0<=score<=100:
        break
    else:
        print('the score should be greater than 0 and less than 100. Pls input again')
if 90<=score<=100:
    print('you got A')
if 80<=score<90:
    print('you got A-')
if 70<=score<80:
    print('you got B+')
if 60<=score<70:
    print('you got B')
if score<60:
    print('you got F')
