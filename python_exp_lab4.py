import math

# 1. Find the factorial of a given number.

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the number: "))
print(fact(n))


# 2. Find whether the given number is Armstrong number. 

def armstrong(n):
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if n==sum:
        return "It is an Armstrong number"
    else:
        return "It is not an Armstrong number"
n=int(input("Enter the number: "))
print(armstrong(n))

# 3. Print Fibonacci series up to given term.

def fibonacci(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
n=int(input("Enter the number: "))
fibonacci(n)

#4. Write a program to find if given number is prime number or not.

def prime(n):
    if n>1:
        for i in range(2, int(math.sqrt(n))+1):
            if n%i==0:
                return "It is not a prime number"
        else:
            return "It is a prime number"
    else:
        return "It is not a prime number"
n=int(input("Enter the number: "))
print(prime(n))

#5. Check whether given number is palindrome or not.

def palindrome(n):
    temp=n
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    if temp==rev:
        return "It is a palindrome number"
    else:
        return "It is not a palindrome number"
n=int(input("Enter the number: "))
print(palindrome(n))

#6. Write a program to print sum of digits.

def sum_of_digit(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n=n//10
    return sum
n=int(input("Enter the number: "))
print(sum_of_digit(n))

#7. Count and print all numbers divisible by 5 or 7 between 1 to 100.

def divisible(n):
    for i in range(1,n+1):
        if i%5==0 or i%7==0:
            print(i)
n=100
divisible(n)

#8. Convert all lower cases to upper case in a string.

def strings(s):
    return s.upper()
s=input("Enter the string: ")
print(strings(s))

#9. Print all prime numbers between 1 and 100. 

def prime(n):
    for i in range(2,n+1):
        if i>1:
            for j in range(2, int(math.sqrt(i))+1):
                if i%j==0:
                    break
            else:
                print(i)
n=100
prime(n)

#10. Print the table for a given number:  
#   5 * 1 = 5 
#   5 * 2 = 10………..


def table(n):
    for i in range(1,11):
        print(n,"x",i,"=",n*i)
n=int(input("Enter the number: "))
table(n)