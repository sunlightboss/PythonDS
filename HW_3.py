def task1():
    str1 = "sdnvck"
    str2 = "d;fvdssc"
    string1 = str1 + str2

def task2():
    str_ = "dlkfnkx"
    string2 = str_ * 3

def task3():
    string = 'Data Science is about working with big data'
    string3 = string.replace('a', '#')
    print(string3)

def task4():
    name = input()
    surname = input()

    print(f'{name} {surname} - Отличный студент!')

def task5():
    code = input()
    code = '0' + code
    slovar = {'01':'Bishkek', '02': 'Osh', '03': 'Batken', '04': 'Jalal-Abad', '05':'Naryn', '06': 'Osh oblast', '07': 'Talas', '08': 'Chuy'}
    if code in slovar:
        print(slovar[code])
    else:
        print('Unknown')

def task6():
    string6 = input()
    if string6.isupper():
        print('Uppercase')
    elif string6.islower():
        print('Lowercase')
    else:
        print('Other')

def task7():
    string7 = input()
    if string7.isdigit():
        print('is digit')
    if string7.isalpha():
        print('is alpha')

def task8():
    string8 = input()
    bool1 = string8[0:12] == "Data Science"
    if bool1:
        print(True)
    else:
        print(False)

def task9():
    string = input()
    string9 = string[-1] + string[1:-1] + string[0]

    print(string9)

def task10():
    string = input()
    string = string[::-1]

    print(string)
task10()








