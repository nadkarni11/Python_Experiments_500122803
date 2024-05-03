#1. Check whether given number is divisible by 3 and 5 both.

def check(n):
    if n%3==0 and n%5==0:
        return True
    else:
        return False
n=int(input("Enter the number: "))
print(check(n))

#2.Check whether a given number is multiple of five or not.

def check(n):
    if n%5==0:
        return True
    else:
        return False
n=int(input("Enter the number: "))
print(check(n))

#3. Find the greatest among two numbers. If numbers are equal than print “numbers are equal”.

def greatest(a,b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return "Numbers are equal"
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
print(greatest(a,b))

#4. Find the greatest among three numbers assuming no two values are same.

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
print(greatest(a,b,c))

#5. Check whether the quadratic equation has real roots or imaginary roots. Display the roots.

def roots(a,b,c):
    d=b**2-4*a*c
    if d>0:
        return "Real Roots"
    elif d==0:
        return "Real and Equal Roots"
    else:
        return "Imaginary Roots"
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
print(roots(a,b,c))

#6. Find whether a given year is a leap year or not.

def leap_year(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return "Leap Year"
    else:
        return "Not a Leap Year"
year=int(input("Enter the year: "))
print(leap_year(year))

'''7. Write a program which takes any date as input and display next date of the 
calendar 
e.g. 
I/P: day=20 month=9 year=2005  
O/P: day=21 month=9 year 2005'''

def next_date(day,month,year):
    if year%4==0 and year%100!=0 or year%400==0:
        leap=True
    else:
        leap=False
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        max_days=31
    elif month==4 or month==6 or month==9 or month==11:
        max_days=30
    else:
        if leap:
            max_days=29
        else:
            max_days=28
    if day<max_days:
        day+=1
    else:
        day=1
        if month==12:
            month=1
            year+=1
        else:
            month+=1
    return day,month,year
day=int(input("Enter the day: "))
month=int(input("Enter the month: "))
year=int(input("Enter the year: "))
print(next_date(day,month,year))

#8. Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjects and calculate the percentage.

'''CGPA=percentage/10 
CGPA range: 
0 to 3.4 -> F 
3.5 to 5.0->C+ 
5.1 to 6->B 
6.1 to 7-> B+ 
7.1 to 8-> A 
8.1 to 9->A+ 
9.1 to 10-> O (Outstanding) 
Sample Gradesheet 
Name: Rohit Sharma 
Roll Number: R17234512   
Sem: 1      
Subject name: Marks 
PDS:   
70 
Python:  
80 
Chemistry:  90 
English:  
60 
Physics:  
50 
Percentage: 70% 
CGPA:7.0 
Grade: '''

def grade_sheet():
    name=input("Enter the name: ")
    roll_no=input("Enter the roll number: ")
    sem=input("Enter the semester: ")
    sap=int(input("Enter the SAP ID: "))
    course=input("Enter the course: ")
    pds=int(input("Enter the marks of PDS: "))
    python=int(input("Enter the marks of Python: "))
    chemistry=int(input("Enter the marks of Chemistry: "))
    english=int(input("Enter the marks of English: "))
    physics=int(input("Enter the marks of Physics: "))
    percentage=(pds+python+chemistry+english+physics)/5
    cgpa=percentage/10
    if cgpa>=0 and cgpa<=3.4:
        grade="F"
    elif cgpa>=3.5 and cgpa<=5.0:
        grade="C+"
    elif cgpa>=5.1 and cgpa<=6:
        grade="B"
    elif cgpa>=6.1 and cgpa<=7:
        grade="B+"
    elif cgpa>=7.1 and cgpa<=8:
        grade="A"
    elif cgpa>=8.1 and cgpa<=9:
        grade="A+"
    else:
        grade="O (Outstanding)"
    return name,roll_no,sem,pds,python,chemistry,english,physics,percentage,cgpa,grade