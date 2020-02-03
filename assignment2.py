# -*- coding: utf-8 -*-
"""
assignment 2
Created on Fri Nov  1 10:37:37 2019

@author: DELL
"""

"""Question 1:write a fn which takes number as argument
 if the number is prime return the number otherwise return next prime"""


def prime(n):
    a=n
    f=0
    for i in range(2,n):
        if a%i==0:
            f=1
    if f!=1:
        print(a)
    else:
        prime(n+1)
prime(8)


"""Questin 2: write a function which takes 4 numbers as argument 
and return min max and avg"""
def mam(a,b,c,d):
    w=a
    x=b
    y=c
    z=d
    avg=(w+x+y+z)/4
    mn=min(w,x,y,z)
    mx=max(w,x,y,z)
    print(avg)
    print(mn)
    print(mx)

mam(1,2,3,4)

"""Question 3: write a fn which takes one number as argument
if the number is perfect square then return the number otherwise return
which min number to be added to get next perfect square"""


def sqrt(a):
    n=a
    f=0
    cnt=0
    for i in range(1,n):
        if i*i==n:
            f=1
            break
    if f==1:
        print(n)
    else:
        cnt=cnt+1
        sqrt(n+1)
        print(cnt)
    
sqrt(10)


"""question:4 write fn to find area of the cone with pi as default argument"""
import cmath
def area(p=3.14):
    pi=p
    r=3
    h=5
    l=cmath.sqrt(r*r+h*h)
    a=pi*r*(r+l)
    print(a)
area()

"""Question:5 write fn to take three values as arguments then find whether it
forms the triangle,is it is forms then return circumscribed circle,
inscribed circle otherwise return 'with provided values triangle cant formed' """
import math
def tri(x,y,z):
    a=x
    b=y
    c=z
    if a+b>c and a+c>b and b+c>a:
        print("this values can form triangle")
        s=(a+b+c)/2
        
        ri=math.sqrt((s-a)*(s-b)*(s-c)/s)

        rc=(a*b*c)/math.sqrt((a+b+c)*(b+c-a)*(a+b-c)*(a+c-b))
        
        print("radius of inscribe circle is",ri)
        print("radius of circumscribe circle is",rc)
    else:
        print("this values can't form triangle")
tri(15.6,20.4,22.5)
    
















