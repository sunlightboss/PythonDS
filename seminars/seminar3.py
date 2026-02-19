def task1():
    a = 32
    b = 3.5
    x = True

    a = str(a)
    b = str(b)
    x = str(x)

    return a,b,x

def task2():
    str_ = input()
    print(str_)

def task3():
    name = input('Write your name:')
    surname = input('Write your surname:')
    print(f'You are {name} {surname}')

def task4():
    name = input('Write your name:')
    surname = input('Write your surname:')
    full_name = name + " " + surname
    print(f'You are {full_name}')

def task5():
    name = input('name - ')
    score = input('score - ')

    print(f'Hello, {name, }your score is {score} ')

def task6():
    name = input('name - ')
    age = input('age - ')

    print(f'Hello my name is {name,} I am {age} years old ')

def task7():
    str_ = 'python is easy'
    print(str_[0])
    print(str_[-1])
    print(str_[0:2])
    print(str_[-1:-4:-1], str_[2:5], str_[1:7], str_[1:-1], str_[0::2], str_[1::2])
    print(str_[::-1], str_[-1:0:-1])

def task8():
    str_ = "PythonProgrammingLanguage"
    pyt = str_[0:6]
    lang = str_[-1:-9:-1]
    lang = lang[::-1]

    res = pyt + " " + lang

    print(res)

def task9():
    str_ = "I love Python programming!"
    str_ = str_.replace('Python', 'Java')
    print(str_)

def task10():
    name = input('Name - ')
    print(f'Hi, {name.capitalize()} !' )

def task11():
    code = 'atgcaagttgacaattta'
    code = code.upper()

def task12():
    code = 'augcaagugacaauuua'
    code = code.replace('u', 't')

    print(code)

def task13():
    nun_phone = '   +7(919)-@784-54_18@@     '
    nun_phone = nun_phone.strip()
    nun_phone = nun_phone.strip('@')
    print(nun_phone)

def task14():
    str_ = '67dg#uin_87'
    ind = str_.index('#')
    print(ind)


def task15():
    name = input()

    text = """ Имя этого героя "name". Поход в театр для него целый ритуал. Входя в фойе, "name" демонстративно снимает шляпу, поправляет галстук и вешает
    ольто на руку. Он непременно думает, что все, кому он знаком говорят про себя: "Ах, сегодня "name" неотразим!" После чего "name"
    занимает лучшее место бенуара и с важным видом достает очки."""

    text = text.replace('name', name)
    print(text)

def task16():
    str_ = '84hj#55hjl'
    str_ = str_[0:5] + 'abc' + str_[5:]
    print(str_)

def task17():
    tel = '0777784500'
    tel = '+996' + tel[1:]
    print(tel)

def task18():
    str_ = input('Write something: ')
    if len(str_) > 5:
        print('too long')

def task19():
    str_ = input('Write something: ')
    if len(str_) > 5:
        str_new = input('Write it again')
        if str_new == str_:
            print(str_)
        else:
            print('Wrong')

def task20():
    password = input()
    symbols = ['#', '@', '%']
    if any(sym in password for sym in symbols):
        print('Good password')
    else:
        print('Bad password')


def task21():
    password = input()
    symbols = ['#', '@', '%']
    if any(sym in password for sym in symbols):
        print('Good password')
    else:
        print('Bad password, write again')
        password = input()
        if any(sym in password for sym in symbols):
            print('password saved')
        else:
            print('You have exhausted the number of attempts')


def task22():
    name_list = """  'айданургулсайкалаймээржылдызбакытайчолпонмадинажаныбекбекжолдостукэлиябатыржанаталмазбекчингизталанталтынбекмаратсаматтайырбеказаматбекмуратасанбек'"""
    name = input()
    if name.lower() in name_list:
        print('Вы получаете стипуху')
    else:
        print('у вас нет стипухи')

def task23():
    code = 'GGGGGGGGGAATTATGATCCTTACTTT'
    if code[0] == 'G':
        code = 'A' + code[1:]
    amount = code.count('G')
    if amount < 5:
        code = code + 'GGG'

    print(code)

def task24():
    name_list = []
    for i in range(2):
        name = input('name - ')
        name_list.append(name)

    print(f'{name_list[0]} \n{name_list[1]}')

def task35():
    brand = 'Acer, Asus, Honor, HP, Lenovo'
    price = '20 000, 35 000, 50 000, 40 000, 25 000'
    brand = brand.split(',')
    price = price.split(',')

    want = input('What you want - ')
    if want.capitalize() not in brand:
        print('No tovar')
    else:
        print(f""" 
    i3:   {price[0]} сом.
    i5:   {price[1]} сом.
    i7:   {price[2]} сом.""")






task35()



