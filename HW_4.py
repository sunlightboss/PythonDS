def task1():
    list_ = [12,2132,1232,32,45565]
    list1 = list_[2]

    print(list1)

def task2():
    list_ = [5, 3, 1, -1, 10]
    list_.sort()
    list_.pop(len(list_)//2)
    print(list_)

def task3():
    list_ = [1, 22, 3, 45, 22, 4, 89, 87, 87, 4]
    num = int(input())
    list3 = list_.count(num)
    print(list3)

def task4():
    korzina = []
    for i in range(5):
        x = input()
        korzina.append(x)
    print(korzina)
    change = int(input('Which one you want to change - '))
    what = input('What you want to add')
    korzina[change-1] = what

    print(korzina)

def task5():
    list_ = []
    for i in range(1,20):
        list_.append(i)
    print(list_)

def task6():
    ls1 = [12324,647656,25436]
    ls2 = [2,13243565,4534,32,43453]
    list6 = ls1 + ls2
    list6 = sum(list6)
    print(list6)

def task7():
    list_ = [1, 2, 3, 10, 100, 12, 4]
    def more(num):
        return num > 10
    list7_iterator = filter(more, list_)
    list7 = list(list7_iterator)

    print(list7)

def task8():
    str_ = 'Data science is good!'
    str_ = str_.split()
    print(str_)



