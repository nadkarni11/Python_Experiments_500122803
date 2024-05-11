# 1. Scan n values in range 0-3 and print the number of times each value has occurred.

def occurence(n):
    d={}
    for i in range(n):
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
n=int(input("Enter the range: "))
print(occurence(n))

# 2. Create a tuple to store n numeric values and find average of all values. 

def average(n):
    sum=0
    for i in range(n):
        sum+=int(input("Enter the value: "))
    return sum/n
n=int(input("Enter the range: "))
print(average(n))

# 3. WAP to input a list of scores for N students in a list data type. Find the score of the 
#runner-up and print the output. 
#Sample Input 
#N = 5 
#Scores= 2 3 6 6 5 
#Sample output 
#5 
#Note: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. 
#Hence, we print 5 as the runner-up score.

def runner_up(n):
    scores=[]
    for i in range(n):
        scores.append(int(input("Enter the score:")))
    scores.sort()
    print("The List of Score is:",scores)
    return scores[-2]
n=int(input("Enter the range:"))
print("The Runner up is:",runner_up(n))

# 4. Create a dictionary of n persons where key is name and value is city.  
#a) Display all names 
#b) Display all city names 
#c) Display student name and city of all students. 
#d) Count number of students in each city.

def persons(n):
    d={}
    occurence={}

    for i in range(n):
        name=input("Enter the name:")
        city=input("Enter the city:")
        d[name]=city
    print("The names are:",d.keys())
    print("The city names are:",d.values())
    print("The student name and city are:",d)
    print("The number of students in each city are:",occurence(n))
n=int(input("Enter the range:"))
persons(n)

'''5. Store details of n movies in a dictionary by taking input from the user. Each movie 
must store details like name,  year, director name, production cost, collection made 
(earning) & perform the following :- 
a) print all movie details 
b) display name of movies released before 2015 
c) print movies that made a profit. 
d) print movies directed by a particular director.'''

def movies(n):
    d={}
    for i in range(n):
        name=input("Enter the name of movie:")
        year=int(input("Enter the year of movie:"))
        director=input("Enter the director of movie:")
        production_cost=int(input("Enter the production cost of movie:"))
        collection=int(input("Enter the collection of movie:"))
        d[name]=[year,director,production_cost,collection]
    print("The movie details are:",d)
    print("The name of movies released before 2015 are:",[i for i in d if d[i][0]<2015])
    print("The movies that made profit are:",[i for i in d if d[i][3]>d[i][2]])
    director=input("Enter the director name:")
    print("The movies directed by director are:",[i for i in d if d[i][1]==director])
n=int(input("Enter the range:"))
movies(n)