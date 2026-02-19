import numpy as np

def matrix(n):
    arr = np.arange(1,n**2+1).reshape(n, n)
    return arr



def matrix2():
    arr = matrix(4)
    print(arr[0,:])
    print(arr[1])
    print(arr[:, 2])
    print(arr[:,2:])


def matrix3():
    arr = matrix(4)
    ind = []


def task10():
    x = np.random.randint(150,200,200)
    mask1 = x > 175
    mask2 = x < 190

    print(x[mask1 & mask2])


task10()
