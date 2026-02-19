import math

def task1():
    num1 = int(input("Number 1 - "))
    num2 = int(input("Number 2 - "))

    number1 = num1 + num2

    print(number1)


def task2():
    num1 = int(input("Number 1 - "))
    num2 = int(input("Number 2 - "))

    number2 = num1//num2
    print(number2)


def task3():
    num1 = int(input("Number 1 - "))
    num2 = int(input("Number 2 - "))

    num3 = num1%num2
    print(num3)

def task4():
    float_num1 = input("Number 1 - ")
    float_num1 = float(float_num1)

    float_num2 = input("Number 2 - ")
    float_num2 = int(float_num2)

    float_num3 = input("Number 3 - ")
    float_num3 = int(float_num3)

    num4 = float_num1*float_num2/float_num3
    print(num4)


def task5():
    osnova = input("What number to 3rd power - ")
    osnova = float(osnova)

    float_num = pow(osnova, 3)
    num5 = float_num/2
    print(num5)


def task6():
    float_number1 = input("1 - ")
    float_number1 = float(float_number1)

    float_number2 = input("2 - ")
    float_number2 = float(float_number2)

    num6 = math.floor(float_number1 - float_number2)
    print(num6)

def task7():
    number1 = input("1 - ")
    number1 = float(number1)

    number2 = input("2 - ")
    number2 = float(number2)

    num7 = math.ceil(number1 - number2)
    print(num7)


def task8():
    a = float(input("a - "))
    b = float(input("b - "))

    num8 = math.hypot(a,b)
    print(num8)


def task9():
    pos_num = -abs(float(input("Positive - ")))
    neg_num = -(abs(float(input("Negative"))))

    num9 = abs(pos_num) + abs(neg_num)
    print(num9)


def task10():
    temp = 90
    num10 = (9/5) * temp + 32

    print(num10)


def task11():
    num11 = (((6+7/12)-(3+17/36))*2.5-(4+1/3)/0.65)/(4/(1/4)-0.5)
    print(num11)


def task12():
    num12 = (((2+3/4)/1.1 +(3+1/3))/(2.5-0.4*(3+1/3)))/(5/7) - ((2+1/6)+4.5)*0.375/2.75 -(1+1/2)
    print(num12)


def task13():
    num13 = 11.4+7.5*(285.6/14-(1+23/30)+(13/50))/(24.4-10.23)
    print(num13)


def task14():
    numb14 = ((9 - 5 + 3 / 8) * (4 - 5 / 12 - 4 / (2 + 2 / 3)) + (3 / 10 - 0.5 * 4)) * (4 / 7) / (
                1 / 24 + 0.25 / (13 + 1 / 3))
    print(numb14)


def task15():
    x = 5.75
    y = x * 40
    print(y)


def task16():
    numerator = 0.16 * (3.2 - 3 / 40) + (2 + 3 / 11) * 4.125 / (3 + 3 / 4)
    denominator = (5 + 1 / 6) * 0.3 - 0.3 * 4.5 + (1 / 3) * 0.3
    value = numerator / denominator

    result = value * 0.4
    print(result)









