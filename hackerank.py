# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 10:52:26 2020

@author: DELL
"""



# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    
    



result = sockMerchant(n, ar)
print(result)

n = int(input("enter number"))
ar=[]
for i in range(0,n):
    ar.append(int(input()))
li=[]
ress=[]
for i in ar:
    if i not in li:
        li.append(i)
for i in li:
    sum=0
    for j in ar:
        if i==j:
            sum+=1      
    ress.append(sum)
res=0
for i in ress:       
    res+=(i//2)
return(res)




def countingValleys(n, s):
    step=0
    cnt=0
    for i in s:
        if step==0 and i=='d':
            cnt+=1
        if i=='u':
            step+=1
        else:
            step-=1
    return(cnt)


n = int(input())

s = input()

result = countingValleys(n, s)
