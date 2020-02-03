# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:16:41 2019
python assignment 1
@author: DELL

"""

"""Question 1Write a program which will find all such numbers which are divisible
 by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single 
line.
Hints:
Consider use range(#begin, #end) method"""

l=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        l.append(i)

print(l)

"""Question 2 Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
Hints:
In case of input data being supplied to the question, it should be assumed to
 be a console input."""
f=1
l1=[1,2,3,4,5]
l2=[]
for i in l1:
   f=f*i
   l2.append(f)
print(l2)
   
"""Question 3 With a given integral number n, write a program to generate a 
dictionary that contains (i, i*i) such that is an integral number between 1 
and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
Hints:
In case of input data being supplied to the question, it should be assumed 
to be a console input.
Consider use dict() """

dic={}
n=int(input("number"))
for i in range(1,n+1):
    dic[i]=i*i
print(dic)

"""Question 4 Write a program which accepts a sequence of comma-separated 
numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
Hints:
In case of input data being supplied to the question, it should be assumed 
to be a console input.
tuple() method can convert list to tuple """"

li=[]
n=int(input("how many number"))
for i in range(0,n):
    i=int(input("NO:"))
    li.append(str(i))
t=tuple(li)
print(li)
print(t)

"""Question 5  Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
Hints:
Use __init__ method to construct some parameters
Hi folks, please try to solve above 5 assignment questions...  """
class Ustr:
    def __init__(self):
        n=str(input("enter the string"))
        print(n.upper())
obj=Ustr()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    