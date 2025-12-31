def task1():
    key = 2302
    value = 'Nurseit'
    dict_ = {key: value}
    print(dict_)


def task2():
    key = input()
    value = input()
    score_dict = {key: value}
    print(score_dict)


def task3():
    dict_ = {123: 'Moskow', 234: 'New-York', 532: 'Dublin',
             554: 'Neapol', 653: 'Paris', 234: 'Sarov', 564: 'Tokmak'}
    dict_[532] = "Stambul"
    print(dict_)


def task():
    score_dict = {}
    next = input()
    while next == 'next':
        name = input()
        score = int(input())
        score_dict[name] = score
        next = input()
        if next == 'stop':
            break

    print(score_dict)

def task7():
    list_ = [3, 5, 4, 6, 5, 3, 12, 13, 14, 35, 46, 57, 46, 35]
    stat = {}
    stat['count'] = len(list_)
    stat['min'] = min(list_)
    stat['mean'] = sum(list_)/len(list_)
    stat['max'] = max(list_)
    stat['sum'] = sum(list_)
    print(stat)


def task19():



