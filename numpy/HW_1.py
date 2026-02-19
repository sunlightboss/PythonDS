import numpy as np
from numpy.ma.core import shape


def task1():
    arr = np.array([[i*j for j in range(1,11)] for i in range(1,11)])
    print(arr)

def task2():
    row_1 = [1, 2, 3, 4]
    row_2 = [5, 6, 7, 8]
    row_3 = [9, 10, 11, 12]
    row_4 = [13, 14, 15, 16]
    arr = np.array([row_1, row_2, row_3, row_4])
    print(arr)

def task3():
    column_1 = np.random.randint(20, 40, 5)
    column_2 = np.random.randint(2, 40, 5)
    arr = np.array([column_1, column_2])
    arr = arr.transpose()
    print(arr)

def task4():
    arr1 = np.zeros(10)
    arr2 = np.ones((5,8), dtype=np.int32)
    arr3 = np.arange(10,26  ,1)

    arr4 = np.array([i for i in range(1,20)], dtype=np.uint8)
    mask = arr4 % 2 == 1
    arr4 = arr4[mask]

    arr5 = np.arange(1, 65).reshape(8,8)

    print(arr1)
    print(arr2)
    print(arr3)
    print(arr4)
    print(arr5)



def task5():
    arr1 = np.arange(1,37,1).reshape(6,6)

    slice1 = arr1[0,1]
    slice2 = arr1[1,0:]
    slice3 = arr1[1:4,1:4]
    slice4 = arr1[[1,1,4],[1,3,3]]
    slice5 = arr1[[2, 2, 2, 3],[1, 2, 3, 4]]
    slice6 = arr1[3,3]
    slice7 = arr1[:, 2]
    slice8 = arr1[4:, 4:]
    slice9 = arr1[[0,2,3],[5,1,2]]
    slice10 = np.diag(arr1)
    slice11 = arr1[-1,-1]
    slice12 = arr1[2:-1,3]
    slice13 = arr1[3:-1,:]
    slice14 = arr1[0:3, 3:].diagonal()
    slice15 = np.fliplr(arr1).diagonal()


def task6():
    arr = np.zeros((5,5),np.int32)
    arr[2:4, 2:] = 100
    print(arr)


def task7(n):
    arr = np.zeros((n,n),np.int32)
    for i in range(n):
        arr[i, i] = 1

    print(arr)


def task8(n):
    arr = np.zeros((n, n), np.int32)
    for i in range(n):
        arr[i, i] = np.random.randint(1, n**2)

    print(arr)

def task9(n):
    arr = np.arange(1, (n**2)+1).reshape(n, n)
    arr = np.triu(arr)
    print(arr)


def task10():
    arr = np.random.randint(1, 100, 50)
    mask1 = arr >= 50
    print(arr[mask1])

    mask2 = (arr > 25) & (arr <= 75)
    print(arr[mask2])

    mask3 = (arr <= 20) | (arr >= 80)
    print(arr[mask3])


def task11():
    arr = np.random.randint(1, 100, (20, 20))
    n_rows = arr[0, 0:].__len__()
    n_columns = arr[0:, 0].__len__()
    print(f'Rows - {n_rows}, Columns - {n_columns}')

    mask1 = arr % 2 == 0
    n_even = arr[mask1]
    print(n_even)

task11()
