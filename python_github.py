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
con_int(10)

#PGM NO:14

"""Define a function that can receive two integral numbers in string form and compute their sum
 and then print it in console."""




Define a function that can accept two strings as input and concatenate them and then print it in console.
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 
"Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
"
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 
"Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
"
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
Define a class named American which has a static method called printNationality.
Define a class named American and its subclass NewYorker. 
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"Please raise a RuntimeError exception.

Hints:

Use raise() to raise an exception."
Write a function to compute 5/0 and use try/except to catch the exceptions.
Define a custom exception class which takes a string message as attribute.
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
"Assuming that we have some email addresses in the ""username@companyname.com"" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

google"
Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
Print a unicode string "hello world".
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
Write a special comment to indicate a Python source code file is in unicode.
"Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

3.55"
"Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

500"
"The Fibonacci Sequence is computed based on the following formula:


f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

13
"
"The Fibonacci Sequence is computed based on the following formula:


f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

0,1,1,2,3,5,8,13
"
"Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10"
"Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

100

Then, the output of the program should be:

0,35,70"
Please write assert statements to verify that every number in the list [2,4,6,8] is even.
"Please write a program which accepts basic mathematic expression from console and print the evaluation result.

Example:
If the following string is given as input to the program:

35+3

Then, the output of the program should be:

38"
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
"Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.


Hints:
Use if/elif to deal with conditions."
Please generate a random float where the value is between 10 and 100 using Python math module.
Please generate a random float where the value is between 5 and 95 using Python math module.
Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
"
Please write a program to randomly print a integer number between 7 and 15 inclusive."
"
Please write a program to compress and decompress the string ""hello world!hello world!hello world!hello world!""."
Please write a program to print the running time of execution of "1+1" for 100 times.
Please write a program to shuffle and print the list [3,6,7,8].
"Please write a program to generate all sentences where subject is in [""I"", ""You""] and verb is in [""Play"", ""Love""] and the object is in [""Hockey"",""Football""].

Hints:
Use list[index] notation to get a element from a list.
"
Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
"By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list."
"By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple."
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
"By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple."
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
Please write a program which count and print the numbers of each character in a string input by console.
"Please write a program which accepts a string from console and print it in reverse order.

Example:
If the following string is given as input to the program:

rise to vote sir

Then, the output of the program should be:

ris etov ot esir"
Please write a program which accepts a string from console and print the characters that have even indexes.
Please write a program which prints all permutations of [1,2,3]
"Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions."

