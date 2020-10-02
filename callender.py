# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:23:50 2019

@author: DELL
"""

#infinte callender

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











class Callender:
    def __init__(self,d,m,y):
        self.dd=d
        self.mm=m
        self.yy=y
        
        rmyr=odyr(self.yy)
        
        od=odrm(rmyr)
        
        li=[31,28,31,30,31,30,31,31,30,31,30,31]
        sm=0
        for i in range(0,self.mm-1):
            sm=sm+li[i]
        sm=sm+self.dd
        sm=sm%7
    
        odd=od+sm
        to=odd%7
    
        days=["Sunday.","Monday.","Tuesday.","Wednesday.","Thursday.","Friday.","Saturday."]
        
        print("The day is..",days[to])
        
        
    def odyr(self,a):
        year=a-1
        
        x=year//400
        x=x*400
        
        year=year-x
        
        return(year)
        
     
    def odrm(self,b):
        ry=b
        if ry<100:
            dy=ry
            odd=rod(dy)+0
        elif ry>100 and ry<200:
            dy=ry-100
            odd=rod(dy)+5
        elif ry>200 and ry<300:
            dy=ry-200
            odd=rod(dy)+2
        elif ry>300 and ry<400:
            dy=ry-300
            odd=rod(dy)+1
        
        return(odd)
    def rod(c):
        dy=c
        lep=dy//4
        ordn=dy-lep
        odd=(lep*2+ordn)%7
        return(odd)
    
    

        
    
obj=Callender(27,3,1996)     
obj.odyr()
obj.odrm()







def cal(d,m,y):
    dd=d
    mm=m
    year=y
    
    yy=year-1
    
    
    if year<2000:
        ry=yy-1600
    else:
        ry=yy-2000
        
        
    
        
    
cal(5,4,2003)






def odyr(a):
        year=a-1
        
        x=year//400
        x=x*400
        
        year=year-x
        
        return(year)

odyr(1996)









