class CandyBox:
    def __init__(self, candies):
        self._candies = 0
        self.candies = candies

    @property
    def candies(self):
        return self._candies

    @candies.setter
    def candies(self, value):
        if value < 0:
            print('Error')
            return
        self._candies = value


class Box:
    def __init__(self, weight):
        self.weight = weight

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


class Dog:
    def speak(self):
        return 'Gav'

class Robot:
    def speak(self):
        return 'Big Boob'

things = [Dog(), Robot()]
for i in things:
    print(i.speak())
