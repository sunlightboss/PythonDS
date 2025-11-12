# factorial

def fact():
    x = int(input())
    y = 1
    for i in range(1, x+1):
        y = y * i
        print(y)


def summ():
    x = int(input())
    res = 0
    for i in range(1, x + 1):
        y = i**2 - i
        res += y
        print(res)
summ()