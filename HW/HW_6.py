def task22():
    ls = [[0], [1, 2], [3, 5], [5, 6], [7, 8, 9]]
    length = []
    for i in ls:
        length.append(len(i))
    idx_max = length.index(max(length))
    idx_min = length.index(min(length))
    print(f' Longest list - {ls[idx_max]}, Shortest list - {ls[idx_min]}')


def task23():
    ls = [20, -40, 30, -20, 20, 30, 40, 50, 20, 60, 60, -70, -20]
    doubles = [x for x in set(ls) if ls.count(x) > 1]
    print(doubles)


def task24():
    nums = ['one', 'two', 'three', 'four', 'five']
    smun = []

    for i in nums:
        i = i[::-1]
        smun.append(i)

    print(smun)


def task25():
    task_25 = [[0, 2, 4, 5], [1, 2, 2, 8, 9], [3, 5, 3], [5, 6, 9, 12], [7, 82, 12, 9]]
    task_25 = [[x for x in sub if x % 2 != 0] for sub in task_25]

    print(task_25)


def task26():
    ls = ['one', 'two', 'three', 'four', 'five']
    task_26 = [x.upper() for x in ls]
    print(task_26)


def task27():
    list_ = [2, 4, 97, 20, 10, 35, 23, 10, 1000]
    task_27 = list_[0]
    for x in list_:
        if x < task_27:
            task_27 = x

    print(task_27)

