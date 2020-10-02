# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:20:12 2020

@author: DELL
"""

#prgm  to find LCM

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

#pgrm to remove duplicate forme array

li=[1,2,3,4,5,6,2,3,5]
rd=[]
for i in range(0,len(li)):
    if rd.count(li[i])==0:
        rd.append(li[i])  
print(rd)
    

# write  apgm to o/p a randome number between 0 and 100 which is divisible by 5&7
#iclusive randome module and list comprehension

import random

xy=[x for x in range(1,10) if x%5==0 and x%7==0]

print(random.choice(xy))
