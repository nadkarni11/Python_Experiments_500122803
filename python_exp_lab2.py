#1. Declare these variables (x, y and z) as integers. Assign a value of 9 to x, Assign a 
#value of 7 to y, perform addition, multiplication, division and subtraction on these 
#two variables and Print out the result. 

x=9
y=7
z=x+y
print(z)
z=x-y
print(z)
z=x*y
print(z)
z=x/y
print(z)

#2. Write a Program where the radius is taken as input to compute the area of a circle.

def ar_circle(r):
    return 3.14*r*r
r=int(input("Enter the radius: "))
print(ar_circle(r))

#3.Write a Python program to solve (x+y)*(x+y)

def solve(x,y):
    return (x+y)*(x-y)
x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
print(solve(x,y))

#4.Write a program to compute the length of the hypotenuse (c) of a right triangle using Pythagoras theorem.

def hypotenuse(a,b):
    return(a**2+b**2)
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b:"))
print("The length of the right Triangle is:", hypotenuse(a,b))

#5.Write a program to find simple interest.

def simple_interest(p,r,t):
    return(p*r*t)/100
p=int(input("Enter the value of p: "))
r=int(input("Enter the value of r: "))
t=int(input("Enter the value of t: "))
print("The simple interest is:", simple_interest(p,r,t))

#6. Write a program to find area of triangle when length of sides are given. 

def ar_triangle(a,b,c):
    s=(a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
print("The area of the triangle is:", ar_triangle(a,b,c))