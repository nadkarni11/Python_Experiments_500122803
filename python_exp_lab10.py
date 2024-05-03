#1. Create numpy array to find sum of all elements in an array.

import numpy as np

def sum_of_elements():
    arr = np.array([1, 2, 3, 4, 5])
    print(f'Sum of all elements in the array: {arr.sum()}')

def main():
    sum_of_elements()

if __name__ == '__main__':
    main()

'''2.  Create numpy array of (3,3) dimension. Now find sum of all rows & columns 
individually. Also find 2nd maximum element in the array.  '''

import numpy as np

def sum_of_rows_columns():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f'Array:\n{arr}')
    print(f'Sum of all rows: {arr.sum(axis=1)}')
    print(f'Sum of all columns: {arr.sum(axis=0)}')
    print(f'Second maximum element in the array: {np.partition(arr.flatten(), -2)[-2]}')

def main():
    sum_of_rows_columns()

if __name__ == '__main__':
    main()

'''3. Perform Matrix multiplication of any 2 n*n matrices. '''

import numpy as np

def matrix_multiplication():
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    print(f'Matrix 1:\n{arr1}')
    print(f'Matrix 2:\n{arr2}')
    print(f'Matrix multiplication:\n{np.dot(arr1, arr2)}')

def main():
    matrix_multiplication()

if __name__ == '__main__':
    main()

'''4.  Write a Pandas program to get the powers of an array values element-wise.  
Note: First array elements raised to powers from second array 
Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]} 
Expected Output: 
X Y Z 
0 78 84 86 
1 85 94 97 
2 96 89 96 
3 80 83 72 
4 86 86 83'''

import pandas as pd

def powers_of_array():
    data = {'X': [78, 85, 96, 80, 86], 'Y': [84, 94, 89, 83, 86], 'Z': [86, 97, 96, 72, 83]}
    df = pd.DataFrame(data)
    print(df)

def main():
    powers_of_array()

if __name__ == '__main__':
    main()

'''5. Write a Pandas program to get the first 3 rows of a given DataFrame. 
Sample Python dictionary data and list labels: 
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 
'Matthew', 'Laura', 'Kevin', 'Jonas'], 
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']} 
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 
Expected Output: 
First three rows of the data frame: 
attempts name qualify score 
a 1 Anastasia yes 12.5 
b 3 Dima no 9.0 
c 2 Katherine yes 16.5 '''

import numpy as np
import pandas as pd

def first_3_rows():
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    df = pd.DataFrame(exam_data, index=labels)
    print('First three rows of the data frame:')
    print(df.head(3))

def main():
    first_3_rows()

if __name__ == '__main__':
    main()

'''6. Write a Pandas program to find and replace the missing values in a given 
DataFrame which do not have any valuable information.'''

import numpy as np
import pandas as pd

def replace_missing_values():
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    df = pd.DataFrame(exam_data, index=labels)
    print('Original DataFrame:')
    print(df)
    df.replace(np.nan, 0, inplace=True)
    print('DataFrame after replacing missing values with 0:')
    print(df)

def main():
    replace_missing_values()

if __name__ == '__main__':
    main()

'''7. Create a program to demonstrate different visual forms using Matplotlib. '''

import matplotlib.pyplot as plt

def visual_forms():
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 30, 40, 50]
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line plot')
    plt.show()

    plt.bar(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Bar plot')
    plt.show()

    plt.scatter(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter plot')
    plt.show()

    plt.hist(y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Histogram')
    plt.show()


def main():
    visual_forms()

if __name__ == '__main__':
    main()
    