# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:50:17 2020

@author: DELL
"""

#PGM NO:1

"""Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line."""


li=[]
for i in range(1000,3001):
    f=0
    t=i
    while t>0:
        r=t%10
        t=t//10
        if r%2!=0:
            f=1
            break
    if f==0:
        li.append(i)
        
print(li)


#PGM NO:2

"""Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3"""


l=0
d=0
sentence=input("enter the string")
for i in sentence:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        l+=1
    

print("The String is..",sentence)
print("LETERS=",l)    
print("digits=",d) 


#PGM NO:3

"""Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9"""

l=0
u=0
sentence=input("enter the string")
for i in sentence:
    if i.islower():
        l+=1
    elif i.isupper():
        u+=1
    

print("The String is..",sentence)
print("lower=",l)    
print("UPPER=",u) 

#PGM NO:3

"""Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106"""


a=int(input("enter the number for a"))
s=a
t=a
for i in range(0,3):
    t=t*10+a
    s=s+t
print(s)

#PGM NO:4

"""Use a list comprehension to square each odd number in a list. The list is input by a sequence
 of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,9,25,49,81..."""

li=[1,2,3,4,5,6,7,8,9]

""" if we need to read list from console
li=[]
n=int(input("enter the number of elements inserted to the list"))
for i in range(0,n):
    i=int(input())
    li.append(i)
"""
sqod=[]
for i in range(0,len(li)):
    if li[i]%2!=0:
        li[i]=li[i]**2
        sqod.append(li[i])
        
print(sqod)

#PGM NO:5

"""Write a program that computes the net amount of a bank account based a transaction log from console input.
 The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500"""

d=0
w=0
t=0
n=1
print()
while n==1:
    inp=input("Hai please click D for Deposit and W for Withdrawal")
    if (inp=='d' or inp=='D'):
        dep=int(input("enter the amount"))
        t=t+dep
    elif (inp=='w' or inp=='W'):
        wid=int(input("enter the amount"))
    
        if t<wid:
            print("Insufficient balance")
        else:
            t=t-wid
    else:
        print("wrong command")
    n=int(input("Succesfull...Do you want to continue...press 1 else press 0"))
    
print("Current balance in your accvount is =",t)


#PGM NO:6

"""A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords 
and will check them according to the above criteria. Passwords that match the criteria are to be printed,
 each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1"""



lower=0
upper=0
dig=0
oth=0
re=[]



    if ()>=6) and (len(li[i])<12 ):
        
        for j in li[i]:
            
            if j.islower():              
                lower+=1
            elif j.isupper():
                upper+=1
            elif j.isdigit():
                dig+=1
            else:
                oth+=1
        if (lower==0 or upper==0 or dig==0):
            flag=1
            
    else:
        flag=1
    if flag==0:
        re.append(li[i])
print(re)
        




#PGM NO:7

"""You are required to write a program to sort the (name, age, height) tuples by ascending order 
where name is string, age and height are numbers. The tuples are input by console.
 The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'),
 ('Tom', '19', '80')]"""

li=[]
y=1
while y==1:
    tup=tuple(input("data").split(','))
    y=int(input("yes=1 or no=0"))
    li.append(tup)
    
print(li.sort())

#PGM NO:8
 
"""Define a class with a generator which can iterate the numbers, which are divisible by 7,
 between a given range 0 and n.

Hints:
Consider use yield"""

    
def gen(a):
        
    i=1
    n=a
        
    while i <= n:
            
        if i % 7==0:
            yield i
                
        i+=1
x=int(input("enter the limit"))
result=gen(x)
    
for i in result:
    print(i)


#PGM NO:9

"""A robot moves in a plane starting from the original point (0,0).
 The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
 The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡
The numbers after the direction are steps. Please write a program to compute the distance from current
 position after a sequence of movement and original point. If the distance is a float, then just print 
 the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:2"""

import math
u=int(input("enter the UPPER steps"))
d=int(input("enter the DOWN steps"))
l=int(input("enter the LEFT steps"))
r=int(input("enter the RIGHT steps"))

ud=u-d
lr=l-r
t=int(math.sqrt(ud**2+lr**2))
    

print("The distance between start and end is ..",t)

#PGM NO:10

"""Write a program to compute the frequency of the words from the input.
 The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1"""


string=input("enter the string")
string=string.split()
li=[]

for i in string:
    
    if i not in li:
        li.append(i)
        
li.sort()
        
for i in li:
    
    print("{}={}".format(i,string.count(i)))
    
    
#PGM NO:11
    
"""Write a method which can calculate square value of number"""


def sqr(n):
    print("square=",n*n)
    
sqr(10)

#PGM NO:12

"""Python has many built-in functions, and if you do not know how to use it, 
you can read document online or find some books. But Python has a built-in document function
 for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function"""
    
    
    
    

#PGM>NO:13
    
"""Define a class, which have a class parameter and have a same instance parameter."""



#PGM NO:14

"Define a function that can convert a integer into a string and print it in console.

def con_int(n):
    n=n
    print("type before conversion is",type(n))
    n=str(n)
    print("type after conversion is",type(n))