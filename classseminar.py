

class Wall:
    def __init__(self, depth, height):
        self.depth = depth
        self.height = height

class Fighter:
    def __init__(self, name, speed, force):
        self.name = name
        self.speed = speed
        self.force = force


class Archer:
    def __init__(self, name, health, num_arrows):
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    def take_hit(self):
        self.health -= 5
        if self.health <= 0:
            print(f'{self.name} id dead')

    def shoot(self, target):
        if self.num_arrows <= 0:
            print(f'{self.name} cant shoot')

        self.num_arrows -= 1
        target.take_hit()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print(f'Hello, {self.name}')


    def birthday(self):
        self.age += 1
        print(self.age)



class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand


class Application:
    def __init__(self, app_id, customer_id, amount):
        self.app_id = app_id
        self.customer_id = customer_id
        self.amount = amount

    def summary(self):
        return f'Application {self.app_id}: customer = {self.customer_id}, amount = {self.amount}'


class CreditApp(Application):
    def __init__(self, app_id, customer_id, amount, term_months):
        super().__init__(app_id, customer_id, amount)
        self.term_months = term_months

    def summary(self):
        base = super().summary()
        return f'{base}, term = {self.term_months} months'

class InstallmentApp(Application):
    def __init__(self, app_id, customer_id, amount, shop_name):
        super().__init__(app_id, customer_id, amount)
        self.shop_name = shop_name

    def summary(self):
        base = super().summary()
        return f'{base}, shop = {self.shop_name}'

