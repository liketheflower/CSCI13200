"""
Due the following class and we will talk the solution at the beginning of the following class.
Please submit it to black board. 

1. we have two variables a and b. a=3, b= 4, what is the output of:
1) a/b
2) a//b
3) a**b
4) a%b
"""
a, b = 3, 4
print('a,b: ',a,b)
print('a/b', a/b)
print('a//b', a//b)
print('a**b', a**b)
print('a%b', a%b)
"""
2. what is the data type of varibale c. Where
    c = "I am not a string"
"""
c = "I am not a string"
print('solution of question 2', type(c))
"""
3. Print out all numbers from 0 to 10(inclusive).
"""
for i in range(0, 11, 1):
    print(i)
"""
4. Print out all even number from 0 to 10(inclusive).
"""
for i in range(0, 11, 2):
    print(i)
"""
5. Print out all even number from 0 to 1000(inclusive).
"""
for i in range(0, 1001, 2):
    print(i)
