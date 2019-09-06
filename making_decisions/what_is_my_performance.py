"""
making decsions
<, > , <=, >= , ==
1<3 and 2>3
"""


score = 100
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
