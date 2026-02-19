def func1():
    print('hello')


def func2(a, b):
    return a + b


def wallet(item, amount):
    return f'На {item} было потрачено {amount} сом'

def func4(s):
    return s.replace(',', '.').replace(' ', '')

#5
def add(a, b):
    return a + b

def div(result, c):
    return result / c


def mult(numbers):
    res = 1
    for x in numbers:
        res *= x
    return res


def str_check(s):
    return 'data science' in s


bd = ['Emil', 'Rena', 'Aliya', 'Hur']

def check(name):
    return 'yes' if name in bd else 'no'

def func9(n):
    return n, n * n


def employee(users):
    return [u['name'] for u in users if u['age'] > 21 and 'IT' in u['work']]


def arg_types(a, b):
    print(type(a))
    print(type(b))


def check_nan(lst):
    if 'nan' in lst:
        return [x for x in lst if x != 'nan']
    return lst