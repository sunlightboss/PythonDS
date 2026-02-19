class Base():
    def __init__(self):
        print('Base self')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A init')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B init')


class C(Base):
    def __init__(self):
        super().__init__()
        print('C init')


class D(A, B, C):
    def __init__(self):
        super().__init__()
        print('D init')


class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Must be more than 0')
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError('Not enough money')
        self.__balance -= amount

    def get_balance(self):
        return self.__balance



