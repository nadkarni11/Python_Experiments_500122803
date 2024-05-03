#1.  Write a program to count and display the number of capital letters in a given string.

def capital(s):
    count=0
    for i in s:
        if i.isupper():
            count+=1
    return count
s=input("Enter the string: ")
print(capital(s))

#2.  Count total number of vowels in a given string. 

def vowels(s):
    count=0
    for i in s:
        if i in "aeiou,AEIOU":
            count=count+1
    return count
s=input("Enter the string: ")
print(vowels(s))

#3.Input a sentence and print words in separate lines.

def words(s):
    return s.split()
s=input("Enter the sentence: ")
print(words(s))

#4.WAP to enter a string and a substring. You have to print the number of times that 
#the substring occurs in the given string. String traversal will take place from left to 
#right, not from right to left. 
#Sample Input 
#ABCDCDC 
#CDC 
#Sample Output 
#2 

def substring(s,sub):
    count=0
    for i in range(len(s)):
        if s[i:i+len(sub)]==sub:
            count+=1
    return count
s=input("Enter the string: ")
sub=input("Enter the substring: ")
print(substring(s,sub))

#Given a string containing both upper and lower case alphabets. Write a Python 
#program to count the number of occurrences of each alphabet (case insensitive) 
#and display the same. 
#Sample Input 
#ABaBCbGc 
#Sample Output 
#2A 
#3B 
#2C 
#1G

def occurence(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
s=input("Enter the string: ")
print(occurence(s))

# 6. Program to count number of unique words in a given sentence using sets. 

def unique(s):
    return len(set(s.split()))
s=input("Enter the sentence: ")
print(unique(s))

# 7. Create 2 sets s1 and s2 of n fruits each by taking input from user and find: 
#a) Fruits which  are in both sets s1 and s2 
#b) Fruits only in s1 but not in s2 
#c) Count of all fruits from s1 and s2

def fruits(s1,s2):
    print("Fruits in both sets: ",s1.intersection(s2))
    print("Fruits only in s1 but not in s2: ",s1.difference(s2))
    print("Count of all fruits from s1 and s2: ",len(s1.union(s2)))
n=int(input("Enter the number of fruits: "))
s1=set()
s2=set()
for i in range(n):
    s1.add(input("Enter the fruit: "))
for i in range(n):
    s2.add(input("Enter the fruit: "))
fruits(s1,s2)

# 8. Take two sets and apply various set operations on them : 
#S1 = {Red ,yellow, orange , blue } 
#S2 = {violet, blue , purple} 

def set_operations(s1,s2):
    print("Union: ",s1.union(s2))
    print("Intersection: ",s1.intersection(s2))
    print("Difference: ",s1.difference(s2))
    print("Symmetric Difference: ",s1.symmetric_difference(s2))
s1={"Red","yellow","orange","blue"}
s2={"violet","blue","purple"}
set_operations(s1,s2)
