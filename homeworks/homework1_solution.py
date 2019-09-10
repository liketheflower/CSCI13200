"""
Due the following class and we will talk the solution at the beginning of the following class.
Please ONLY submit it to black board. 

1. Print hello world 0 to hello world 20 by using loops.
"""
for i in range(21):
    print('hello world ', i)
"""
2. For quesiton 1, skip the hello world 17.
"""
# solution 1
for i in range(21):
    if i == 17:
        continue
    print('hello world ', i)
# solution 2
for i in range(21):
    if i != 17:
        print('hello world ', i)
"""
3. Print 0 to a number which is an even number and greater than 25.
"""
# solution 1
i = 0
while True:
    #i = i+1
    i += 1
    if i>25 and i%2==0:
        print(i)
        break
i = 0
#solution 2
good = True 
while good:
    #i = i+1
    i += 1
    if i>25 and i%2==0:
        good = False
    print(i)
"""
4. input an integer from computer to output your decision of: 1) this number is a negative number 2) this number is a positive number. 3) this number is equal to 0.
"""

number = input('pls input a number')
#print(type(number))
number = int(number)
if number > 0:
    print('positive')
elif number < 0:
    print('negative')
else:
    print('equal to 0')


