# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 21:33:29 2019

@author: favas
"""

1.Find the Non-Repeating Elements in an Array 
Input = [4,3,4,3,1,2,1]
Output = 2 (As 2 is present only once)


li=[4,3,4,3,1,2,1]

for i in li:
    
    if li.count(i) == 1:
        
        print(i)
        
        
2.Find The Immediate Next Largest Number 
Input = [5,7,6,8,4,10]
Output
5 -> 7
7 -> 8
6 -> 8
8 -> 10
4 -> 10
10 -> 1
●For 5 the next largest element on the right is 7
●For 7the next largest number on the right is 8
●Last element always 7                              #have some doubt in this line



inp=[5,7,6,8,4,10]

for i in range(0,len(inp)):
    for j in range(i+1,len(inp)):
        
        if inp[i] < inp[j]:
            print("{}->{}".format(inp[i],inp[j]))
            break;
        
        
        
3.Find The Peak Element in an array 
Input = [5,6,7,4,3,4,1]
Output = 7,4 (*6,4 are the element on either side of 7, since 7>6&4,
7 is a peak element)

ip=[5,6,7,4,3,4,1]

for i in range(1,len(ip)-1): 
    if ip[i-1] < ip[i] and ip[i+1] < ip[i]:
        
        print(ip[i])





                                "THANKYOU!..."