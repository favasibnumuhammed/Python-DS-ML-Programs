# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:34:55 2019

@author: DELL
"""
Program 1:

"""print a-z"""

for  i in range(97,123):
    print(chr(i),i)
    
    
"""print A-Z"""   
for  i in range(65,91):
    print(chr(i),i)
    
Program 2:
        
"""amstrnong of a number"""
x=int(input("enter the no"))
n=x
s=0
while x>0:
    r=x%10
    s+=r**3
    x//=10
print(s)
if s==n:
    print(n,"is amstrong")
else:
    print(n,"is not amstrong")

Program 3:
    
"""even number"""

x=int(input("enter the number "))
if x % 2==0:
    print("the number is even")
else:
    print("the nmber is odd")
    
Program 4:
    
"""factorial of a number """

x=int(input("enter the number"))
f=1
for i in range(1,x+1):
    f=f*i
print(f)

Program 5:
    
"""fibanoci series of a number"""

x=int(input("enter the limit"))
a,b=0,1
print(a)
print(b)
for i in range(2,x):
    c=a+b
    a=b
    b=c
    print(c)
    
Program 6:
    
"""floyd tree"""
x=int(input("number of rows"))
n=1
for i in range(1,x+1):
    for j in range(0,i):
        print(n,end="")
        n+=1
    print()

Program 7:
    
"""leader in array"""


li=[]
x=int(input("enter the number of elements"))
for i in range(0,x):
    i=int(input())
    li.append(i)
print("leaders are....")

for i in range(0,x):
    f=0
    for j in range(i+1,x):
        if li[i] < li[j]:
            f=1
            break
    if f==0:
        print()
        print(li[i])
    
Program 8:
    
"""leap year"""

y=int(input("enter the year"))
n=len(str(y))
if n==4:
    if y%4==0 and y%100!=0 or y%400==0:
        print(y,"is leap year")
    else:
        print(y,"is not leap year")    
else:
    print("an year should have 4 numbers")
    
Program 9:
    
"""paliandrome and reverse"""

x=int(input("enter the number"))
n=x
s=0
while n>0:
    r=n%10
    s=s*10+r
    n//=10
print("reverse=",s)
if s==x:
    print(x,"is a paliandrome")
else:
    print(x,"is not a paliandrome")

Program 10:
    
"""prime or not"""
n=int(input("enter the number"))
f=0
for i in range(i,n//2):
    if n%i==0:
        f=1
        break
if f==1:
    print(n,"is  prime")
else:
    print(n,"is not prime")

Program 11:
    
"""pyramid"""
n=int(input("no of rows"))
k=n
for i in range(1,n+1):
    for s in range(0,k):
        print(" ",end="")
    k-=1
    for j in range(0,i):
        print("* ",end="")
    print()
    
Program 12:
    
"""swapping"""
a=int(input("enter first value"))
b=int(input("enter second value"))
a,b=b,a
print("after swapping....a={} and b={}".format(a,b))

Program 13:
    
"""identifie characters from string"""

strg=input("enter string")
li=[0]
for i in strg:
    li.append(ord(i)-97)
    
print(li)

Program 14:
    
"prgm  to find LCM"

a=int(input("enter the first nmber"))
b=int(input("enter the second nmber"))

for i in range(1,10):
    k=a*i
    
    for i in range(1,10): 
        l=b*i
        if k==l:
            break
    if k==l:
        break
print(k)


#another way

a=int(input("enter the first nmber"))
b=int(input("enter the second nmber"))

for i in range(1,a):
    if a%i==0 and b%i==0:
        gcd=i
        
lcm=(a*b)//gcd

print(gcd)
print(lcm)

Program 15:
    
"pgrm to remove duplicate forme array"

li=[1,2,3,4,5,6,2,3,5]
rd=[]
for i in range(0,len(li)):
    if rd.count(li[i])==0:
        rd.append(li[i])  
print(rd)
    
Program 16:
    
# write  apgm to o/p a randome number between 0 and 100 which is divisible by 5&7
#iclusive randome module and list comprehension

import random

xy=[x for x in range(1,10) if x%5==0 and x%7==0]

print(random.choice(xy))

Program 7:
    
"infinte callender"

def cal(d,m,y):
    dd=d
    mm=m
    year=y
    yy=year-1
    
    x=yy//400
    x=x*400  
    ry=yy-x
#to find the number of odd days in remainig year after leap year like 2000,1600etc
    if ry<100:
        dy=ry
        lep=dy//4
        ordn=dy-lep
        odd=(lep*2+ordn)%7
    elif ry>100 and ry<200:
        dy=ry-100
        lep=dy//4
        ordn=dy-lep
        odd=((lep*2+ordn)%7)+5
    elif ry>200 and ry<300:
        dy=ry-200
        lep=dy//4
        ordn=dy-lep
        odd=((lep*2+ordn)%7)+2
    elif ry>300 and ry<400:
        dy=ry-300
        lep=dy//4
        ordn=dy-lep
        odd=((lep*2+ordn)%7)+1
#form sum of days from january to dd and mm    
    li=[31,28,31,30,31,30,31,31,30,31,30,31]
    sm=0
    for i in range(0,mm-1):
        sm=sm+li[i]
    sm=sm+dd
    sm=sm%7
    odd=odd+sm
    to=odd%7
#can also check it first for feb 29
    if year%4==0:
        to+=1
    
    days=["Sunday.","Monday.","Tuesday.","Wednesday.","Thursday.","Friday.","Saturday."]   
    print("The day is..",days[to])
    
cal(27,3,1996)



