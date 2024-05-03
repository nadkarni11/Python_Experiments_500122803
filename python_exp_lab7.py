#1. Write a Python function to find the maximum and minimum numbers from a sequence of numbers.  (Note: Do not use built-in functions.) 

def max_min(n):
    max=n[0]
    min=n[0]
    for i in n:
        if i>max:
            max=i
        elif i<min:
            min=i
    return max,min
n=[1,2,3,4,5,6,7,8,9]
print(max_min(n))

#2. Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.

def cube(n):
    sum=0
    for i in range(1,n):
        sum+=i**3
    return sum
n=int(input("Enter the number: "))
print(cube(n))

#3. Write a Python function to print 1 to n using recursion. (Note: Do not use loop) 

def print_n(n):
    if n>0:
        print_n(n-1)
        print(n)
n=int(input("Enter the number: "))
print_n(n)

#4. Write a recursive function to print Fibonacci series upto n terms. 

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter the number: "))
for i in range(n):
    print(fibonacci(i))

#5. Write a lambda function to find volume of cone. 

volume=lambda r,h:3.14*r*r*h/3
r=int(input("Enter the radius: "))
h=int(input("Enter the height: "))
print("The volume of cone is:",volume(r,h))

#6. Write a lambda function which gives tuple of max and min from a list. 
#Sample input: [10, 6, 8, 90, 12, 56] 
#Sample output: (90,6) 


max_min=lambda n:(max(n),min(n))
n=list(map(int,input("Enter the numbers: ").split()))
print(max_min(n))

#7. Write functions to explain mentioned concepts: 
#a. Keyword argument 
#b. Default argument 
#c. Variable length argument 

#a. Keyword argument
def keyword(name,age):
    print("Name:",name)
    print("Age:",age)
keyword(name="Ram",age=20)

#b. Default argument
def default(name,age=20):
    print("Name:",name)
    print("Age:",age)
default("Ram")

#c. Variable length argument
def variable(*args):
    for i in args:
        print(i)
variable(1,2,3,4,5)

