class Character:
    def __init__(self, name, start_hp):
        self.name = name
        self._hp = 0
        self.hp = start_hp

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, new_value):
        self._hp = max(0, min(100, new_value))

    def take_damage(self, damage):
        self.hp = self.hp - damage

    def heal(self, amount):
        self.hp = self.hp + amount

    def status(self):
        print(f"{self.name}: HP = {self.hp}")


hero = Character('Batman', 80)
hero.take_damage(50)
hero.status()
hero.heal(40)
hero.status()