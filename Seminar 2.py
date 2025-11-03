def task1():
    num1 = int(input())
    if num1 > 5:
        print(True)
    else:
        print(False)


def task2():
    num1 = int(input())
    if num1 % 2 == 0:
        print(True)
    else:
        print(False)


def task3():
    a = int(input('A - '))
    b = int(input('B - '))
    try:
        if a / b == 2:
            print(True)
        else:
            print(False)
    except ZeroDivisionError:
        print("Нельзя делить на ноль")


def task4():
    num1 = int(input('Num - '))
    if num1 % 3 == 0:
        print('Yes')
    else:
        print('No')


def task5():
    num1 = int(input())
    if num1 % 2 == 0:
        print(num1)
    else:
        num1 = num1 + 1
        print(num1)


def task6():
    num1 = int(input())
    bool1 = num1 > 3
    bool2 = num1 <= 8
    if bool1 and bool2:
        print(True)
    else:
        print(False)

def task7():
    num1 = int(input())
    bool1 = num1 >= 5
    bool2 = num1 < 15
    bool3 = num1 != 10

    if all([bool1, bool2, bool3]):
        print(True)
    else:
        print(False)


def task8():
    num1 = int(input())
    bool1 = num1 <= 5
    bool2 = num1 > 10

    if bool1 and bool2:
        print(True)
    else:
        print(False)


def task9():
    num1 = int(input())
    bool1 = num1 > 2
    bool2 = num1 <= 6
    cond1 = bool1 and bool2
    cond2 = num1 > 10

    if cond1 and cond2:
        print(True)
    else:
        print(False)


def task10():
    num1 = int(input())
    bool1 = num1 < 4
    bool2 = num1 > 10

    bool3 = num1 <= 2
    bool4 = num1 >= 6

    cond1 = bool1 and bool2
    cond2 = bool3 and bool4

    if cond1 and  cond2:
        print(True)
    else:
        print(False)

def task11():
    num1 = int(input())
    bool1 = num1 <= 3
    bool2 = num1 > 5
    if bool1 or bool2:
        print(True)
    else:
        print(False)


def task12():
    def ineq1():
        num1 = int(input())
        bool1 = num1 > -3
        bool2 = num1 <=6
        if bool1 or bool2:
            print(True)
        else:
            print(False)

    def ineq2():
        num1 = int(input())
        bool1 = num1 >= 4
        if bool1:
            print(True)
        else:
            print(False)

    def ineq3():
        num1 = int(input())
        bool1 = num1 > -2
        bool2 = num1 <= 3
        cond1 = bool1 and bool2

        bool3 = num1 > 5
        if any([cond1, bool3]):
            print(True)
        else:
            print(False)

    def ineq4():
        num1 = int(input())
        bool1 = num1 > 0 and num1 < 4
        bool2 = 6 <= num1 < 10
        if any([bool1, bool2]):
            print(True)
        else:
            print(False)

    ineq1()
    ineq2()
    ineq3()
    ineq4()

def task13():
    num1 = int(input())
    bool1 = num1 >= 40
    bool2 = num1 <= 45

    if bool1 and bool2:
        print("Параметры оптимальны")
    elif num1 < 40:
        print('Корабль разрушится в атмосфере')
    elif num1 > 45:
        print('Контролируемый спуск невозможен')

def task14():
    x = int(input('X - '))
    y = int(input('Y - '))

    z = 0.5*x + 4

    print('Higher' if y > z else 'On line' if y == z else 'Below')


def task16():
    num1 = int(input())
    bool1 = num1/pow(num1, 0.5) == 3
    if bool1:
        print(True)
    else:
        print(False)

def task17():
    num1 = int(input())
    num2 = int(input())

    sum1 = num1 + num2
    minus = num1 - num2

    bool11 = sum1 > 0
    bool12 = minus > 0
    cond1 = bool11 and bool12
    bool2 = minus < 0 < sum1
    bool3 = minus > 0 > sum1

    print('++' if cond1 else '+-' if bool2 else '-+' if bool3 else '--')
    print(sum1, minus)


def task18():
    a = int(input())
    b = int(input())
    c = int(input())

    d = b**2 - 4*a*c

    if d > 0:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        print(x1, x2)

    elif d == 0:
        x = -b / (2*a)
        print(x)

    else:
        print('Нет действительных корней')


def task19():
    a = int(input())
    b = int(input())
    c = int(input())

    bool1 = a+b > c
    bool2 = a+c > b
    bool3 = b+c > a

    if all([bool1, bool2, bool3]):
        print(True)
    else:
        print(False)

def task20():
    a = int(input())
    b = int(input())
    c = int(input())

    numbs = []

    if max(a,b,c) == a:
        numbs.append(c)
        numbs.append(b)
        numbs.append(a)

    elif max(a,b,c) == b:
        numbs.append(c)
        numbs.append(a)
        numbs.append(b)

    else:
        numbs.append(a)
        numbs.append(b)
        numbs.append(c)

    square_sum = pow(numbs[0], 2) + pow(numbs[1], 2)
    if square_sum == numbs[2]**2:
        print('Прямоугольный треугольник')
    else:
        print(False)

task20()

