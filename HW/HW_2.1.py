def task1():
    num1 = int(input())
    if num1 > 0:
        print(True)
    else:
        print(False)

def task2():
    # 90> 80-90 70-80 60-70 <60

    mark = int(input())
    bool1 = 80 <= mark < 90
    bool2 = 70 <= mark < 80
    bool3 = 60 <= mark < 70

    if mark >= 90:
        print('5')
    elif bool1:
        print('4')
    elif bool2:
        print('3')
    elif bool3:
        print('Учись чурка')
    else:
        print('Неуд')


def task3():
    nums = []

    for i in range(3):
        x = int(input())
        nums.append(x)

    nums.sort()
    print(nums[0])

def task4():
    x = int(input())
    y = int(input())

    sum1 = x + y
    divide1 = x/y

    if x % y == 0:
        print(divide1)
    else:
        print(sum1)


def task5():
    a = 4
    b = 9
    c = 6

    bool1 = a + b > c
    bool2 = a + c > b
    bool3 = b + c > a

    if all([bool1, bool2, bool3]):
        print(True)
    else:
        print(False)


def task6():
    a = 58
    b = 5
    c = 63

    print('Yes' if a+b == c else 'No')

def task7():
    x = int(input())
    bool1 = x >= 2 and x < 10
    print('Yes' if bool1 else 'No')


def task8():
    x = int(input())
    bool1 = x < 4
    bool2 = x >= 5
    if any([bool1, bool2]):
        print(True)
    else:
        print(False)

def task9():
    nums = [2,4,6,8,10]
    x = int(input())
    if x in nums:
        print(True)
    else:
        print(False)


def task10():
    x = int(input())
    bool1 = -10 < x < 5
    bool2 = 5 < x <= 7
    bool3 = x > 8
    if any([bool1, bool2, bool3]):
        print(True)
    else:
        print(False)


def task11():
    x = int(input())
    if x == -5 or x == 7:
        print("No")
        exit()
    var1 = (x**2 - 3*x)/(x+5)
    var2 = (x-3)/(7-x)
    if var1 >= var2:
        print(True)
    else:
        print(False)


def task12():
    x = int(input())
    var = x**2 - 3*x <= 0
    var2 = x**2 -6*x + 8 > 0
    if var and var2:
        print(True)
    else:
        print(False)

def task13():
    x = int(input())
    var1 = x-3 > 5
    var2 = x <= 2
    if var1 and var2:
        print(True)
    else:
        print(False)





