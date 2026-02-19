# 1st

class Animal():
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def speak(self):
        return 'Animal Sound'


class Dog(Animal):
    def speak(self):
        return 'Woof'

animal = Animal('Alinur')
dog = Dog('Denji')

print(animal.speak(), dog.speak())

# 2nd

def count_words(text: str):
    text =  text.split()
    len1 = len(text)
    return len1

tt = """ hdu hdchj sdvchjij dwgvsbcj gdvfgcckdhbscbwi idsjchb """

print(count_words(tt))


# 3rd

class TextAnalyser():
    def __init__(self, text):
        self.text = text

    def analyze(self, text: str):
        text = text.split()
        len1 = len(text)
        return len1


tt = TextAnalyser(""" hdu hdchj sdvchjij dwgvsbcj gdvfgcckdhbscbwi idsjchb """)
print(tt.analyze(tt.text))



