def mse():
    n = int(input())
    y = list(range(1, 100))
    y_pred = list(range(2, 102))
    summ = 0

    divider = (1/n)

    for i in range(n):
        summ += (y[i] - y_pred[i])**2

    prod = divider*summ
    print(prod)

def stroka():
    str_ = 'abcdefghi123456789'
    print(str_[1], str_[-1], str_[-3], str_[1:3], str_[1:5], str_[-1:-4:-1])


def task_10():
    str_ = 'H12a3ve 34a4 5n65i455ce654 6l45es64s45o6n6'
    digit_list = []
    alpha_list = []

    for i in str_:
        if i.isalpha():
            alpha_list.append(i)
    str_.strip(''.join(alpha_list))
    print(str_)

def task10_1():
    str_ = 'H12a3ve 34a4 5n65i455ce654 6l45es64s45o6n6'
    result = ''.join(ch for ch in str_ if not ch.isalpha())
    dumm = 0
    result = result.replace(' ', '')
    for i in result:
        dumm += int(i)

    print(dumm)



task_10()
task10_1()




