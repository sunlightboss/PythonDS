from cmath import infj
from curses.ascii import isdigit
from operator import index


def task_1():
    task1 = []
    for i in range(100):
        if i % 2 == 1:
            task1.append(i)
    print(task1)

def task_2a():
    list1 = []
    n = input('Введите число - ')
    for i in range(1, int(n)+1):
        list1.append(str(i))
    print(list1)


def task2b():
    task2 = []
    list2 = []
    for i in range(1, 100):
        task2.append(i)
    for j in task2:
        if task2.index(j) % 2 == 0:
            list2.append(j)
        else:
            list2.append(j*10)
    task2 = list2

    print(task2)


def task3():
    task =  [1, 22, 3, 45, 22, 4, 89, 87, 87, 4]
    list_ = []
    for i in range(len(task)):
        if i % 2 == 1:
            list_.append(task[i])
    print(list_)


def task4():
    ls = [11, 23, 45, 7, 9]
    ls = ls[::-1]
    for i in ls:
        print(i)


def task5():
    task_5 = []
    n = int(input('Enter number - '))

    for i in range(1, int(n)+1):
        a = 'ID_000' + str(i)
        if i >= 10 and i <= 99:
            a = 'ID00' + str(i)
        elif i >= 100 and i < 1000:
            a = 'ID0' + str(i)
        elif i >= 1000:
            a = 'ID' + str(i)

        task_5.append(a)

    print(task_5)


def task6():
    a = 'Nurs'
    print(a.split())




def task7():
    users = [23, 24, 43, 25, 83]
    task_7 = []
    for i in users:
        a = 'ID_00' + str(i)
        task_7.append(a)

    print(task_7)


def task8():
    my_str = 'abcdefg12345'
    task_8 = []
    for i in my_str:
        task_8.append(i)
    print(task_8)


def task9():
    results = []
    for i in range(1, 25):
        s = 4*(i**2) + (24-i)**2
        results.append(s)

    print(min(results))


def task10():
    id_list = ['ID_23', 'ID_24', 'ID_43', 'ID_25', 'ID_83']

    task_10 = [int(item.split('_')[1]) for item in id_list]


def task11():
    num_list = [1,3,2,4]
    task_11 = []

    for i in range(0, len(num_list)):
        if i == 0:
            task_11.append(num_list[i+1]+num_list[-1])
        if i == len(num_list)-1:
            task_11.append(num_list[i]+num_list[0])
        else:
            task_11.append(num_list[i+1]+num_list[i-1])


    print(task_11)


def task_12():
    task12 = []
    for i in range(0, 100):
        result = i**2 - 11*i +30
        if result == 0:
            task12.append(i)

    print(task12)


def task13():
    results = []
    for i in range(1, 100):
        s = i**2 - 8*i +3
        results.append(s)

    print(min(results))


def task14():
    task_14 = []
    list1 = []
    for i in range(-100, 100):
        result = i**2 - i - 6
        task_14.append(result)


def task15():
    pass


def task16():
    task_16 = [1, 22, 3, 45, 22, 4, 89, 87, 87, 4]
    for i in range(0, len(task_16)):
        if i % 2 == 1:
            task_16.pop(i)

    print(task_16)





task16()