'''1. Create a class of student (name, sap id, marks[phy,chem,maths] ). Create 3 
objects by taking inputs from the user and display details of all students.'''

class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    def display(self):
        print(f'Name: {self.name}')
        print(f'SAP ID: {self.sap_id}')
        print(f'Physics: {self.marks[0]}')
        print(f'Chemistry: {self.marks[1]}')
        print(f'Maths: {self.marks[2]}')

def main():
    students = []
    for _ in range(3):
        name = input('Enter name: ')
        sap_id = input('Enter SAP ID: ')
        marks = list(map(int, input('Enter marks in Physics, Chemistry, Maths: ').split()))
        students.append(Student(name, sap_id, marks))

    for student in students:
        student.display()

if __name__ == '__main__':
    main()

'''2. Add constructor in the above class to initialize student details of n students and 
implement following methods: 
a) Display() student details 
b) Find Marks_percentage() of each student 
c)  Display result() [Note: if marks in each subject >40% than Pass else Fail]
Write a Function to find average of the class. '''

class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    def display(self):
        print(f'Name: {self.name}')
        print(f'SAP ID: {self.sap_id}')
        print(f'Physics: {self.marks[0]}')
        print(f'Chemistry: {self.marks[1]}')
        print(f'Maths: {self.marks[2]}')

    def marks_percentage(self):
        return sum(self.marks) / 3

    def result(self):
        if all(mark > 40 for mark in self.marks):
            return 'Pass'
        else:
            return 'Fail'
        
def average(students):
    return sum(student.marks_percentage() for student in students) / len(students)

def main():
    students = []
    n = int(input('Enter number of students: '))
    for _ in range(n):
        name = input('Enter name: ')
        sap_id = input('Enter SAP ID: ')
        marks = list(map(int, input('Enter marks in Physics, Chemistry, Maths: ').split()))
        students.append(Student(name, sap_id, marks))

    for student in students:
        student.display()
        print(f'Marks percentage: {student.marks_percentage()}')
        print(f'Result: {student.result()}')

    print(f'Average marks percentage of the class: {average(students)}')

if __name__ == '__main__':
    main()

'''3. Create programs to implement different types of inheritances.'''

# Single inheritance
class A:
    def display(self):
        print('Class A')

class B(A):
    def display(self):
        print('Class B')

def main():
    obj = B()
    obj.display()

if __name__ == '__main__':
    main()

# Multiple inheritance
class A:
    def display(self):
        print('Class A')

class B:
    def display(self):
        print('Class B')

class C(A, B):
    pass

def main():
    obj = C()
    obj.display()

if __name__ == '__main__':
    main()

# Multilevel inheritance
class A:
    def display(self):
        print('Class A')

class B(A):
    def display(self):
        print('Class B')

class C(B):
    pass

def main():
    obj = C()
    obj.display()

if __name__ == '__main__':
    main()

# Hierarchical inheritance
class A:
    def display(self):
        print('Class A')

class B(A):
    pass

class C(A):
    pass

def main():
    obj1 = B()
    obj1.display()
    obj2 = C()
    obj2.display()

if __name__ == '__main__':
    main()


# Hybrid inheritance

class A:
    def display(self):
        print('Class A')

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

def main():
    obj = D()
    obj.display()

if __name__ == '__main__':
    main()

'''4. Create a class to implement method Overriding.'''

class A:
    def display(self):
        print('Class A')

class B(A):
    def display(self):
        print('Class B')

def main():
    obj = B()
    obj.display()

if __name__ == '__main__':
    main()

'''5. Create a class for operator overloading which adds two Point Objects where Point 
has x & y values 
e.g. if 
P1(x=10,y=20) 
P2(x=12,y=15) 
P3=P1+P2 => P3(x=22,y=35)'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'Point(x={self.x}, y={self.y})'
    
def main():
    p1 = Point(10, 20)
    p2 = Point(12, 15)
    p3 = p1 + p2
    print(p3)

if __name__ == '__main__':
    main()

