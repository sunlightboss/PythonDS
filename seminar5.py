def task1():
    for i in range(10):
        print('Java')

def task2():
    # user_input = input()
    # parts = user_input.split(' ')
    # i = 0
    # while i < int(parts[1]):
    #     print(parts[0])
    #     i += 1

    word, count = input().split(' ')
    for i in range(int(count)):
        print(word)


def task3():
    spisok = []
    for i in range(2,14):
        spisok.append(i)
    print(*spisok)

def task4():
    spisok = []
    for i in range(2, 14):
        spisok.append(i)
    print(spisok)

def task5():
    even = []
    num_list = [1, 3, 2, 5, 4, 3, 6, 7, 8, 7, 9, 8]
    for i in num_list:
        if i % 2 == 0:
            even.append(i)
    print(*even)

def task6():
    num_list = [1, 3, 2, 5, 4, 3, 6, 7, 8, 7, 9, 8]
    num_ind = []
    for i in num_list:
        if i % 2 == 0:
            num_ind.append(i)

    num_list = num_ind

    print(num_list)

def task7():
    spisok = []
    for i in range

task6()


