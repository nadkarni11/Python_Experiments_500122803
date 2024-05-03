'''1. Add few names, one name in each row, in “name.txt file”. 
a. Count no of names 
b. Count all names starting with vowel 
c. Find longest name'''

def count_names():
    with open('name.txt', 'r') as file:
        names = file.readlines()
        print(f'Number of names: {len(names)}')
        print(f'Number of names starting with vowel: {len([name for name in names if name[0].lower() in "aeiou"])}')
        print(f'Longest name: {max(names, key=len)}')

def main():
    count_names()

if __name__ == '__main__':
    main()

'''2. Store integers in a file. 
a. Find the max number 
b. Find average of all numbers 
c. Count number of numbers greater than 100'''

def count_numbers():
    with open('numbers.txt', 'r') as file:
        numbers = [int(number) for number in file.readlines()]
        print(f'Max number: {max(numbers)}')
        print(f'Average of all numbers: {sum(numbers) / len(numbers)}')
        print(f'Number of numbers greater than 100: {len([number for number in numbers if number > 100])}')

def main():
    count_numbers()

if __name__ == '__main__':
    main()

'''3. Assume a file city.txt with details of 5 cities in given format (cityname population(in 
lakhs) area(in sq KM) ): 
Example: 
Dehradun 5.78 308.20 
Delhi 190 1484 
…………… 
Open file city.txt and read to: 
a. Display details of all cities 
b. Display city names with population more than 10Lakhs 
c. Display sum of areas of all cities'''

def city_details():
    with open('city.txt', 'r') as file:
        cities = [city.strip().split() for city in file.readlines()]
        print('Details of all cities:')
        for city in cities:
            print(f'City: {city[0]}, Population: {city[1]} Lakhs, Area: {city[2]} sq KM')
        print('City names with population more than 10 Lakhs:', [city[0] for city in cities if float(city[1]) > 10])
        print('Sum of areas of all cities:', sum([float(city[2]) for city in cities]))

def main():
    city_details()

if __name__ == '__main__':
    main()

'''4.  Input two values from user where the first line contains N, the number of test 
cases. The next N lines contain the space separated values of a and b. Perform 
integer division and print a/b. Handle exception in case of ZeroDivisionError or 
ValueError.  
Sample input 
1 0 
2 $ 
3 1  
Sample Output : 
Error Code: integer division or modulo by zero  
Error Code: invalid literal for int() with base 10: '$' 3'''

def integer_division():
    n = int(input('Enter number of test cases: '))
    for _ in range(n):
        try:
            a, b = map(int, input().split())
            print(a // b)
        except ZeroDivisionError:
            print('Error Code: integer division or modulo by zero')
        except ValueError:
            print('Error Code: invalid literal for int() with base 10')

def main():
    integer_division()

if __name__ == '__main__':
    main()

'''5. Create multiple suitable exceptions for a file handling program.'''

def file_handling():
    try:
        with open('file.txt', 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print('File not found')
    except PermissionError:
        print('Permission denied')
    except Exception as e:
        print(f'Error: {e}')

def main():
    file_handling()

if __name__ == '__main__':
    main()

