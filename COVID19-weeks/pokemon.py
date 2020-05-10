class Pokemon:
    basic_attack = 'tackle'
    damage = 40

    def __init__(self, name, trainer):
        self.name, self.trainer = name, trainer
        self.level, self.hp = 1, 50
        self.paralyzed = False

    def speak(self):
        print(self.name + '!')

    def attack(self, other):
        if not self.paralyzed:
            self.speak()
            print(self.name, 'used', self.basic_attack, '!')

        other.receive_damage(self.damage)

    def receive_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
            print(self.name, 'fainted!')


class ElectricType:
    basic_attack = 'thunder shock'
    damage = 40
    prob = 0.1

    def __init__(self, name, trainer):
        self.name, self.trainer = name, trainer
        self.level, self.hp = 1, 50
        self.paralyzed = False

    def speak(self):
        print(self.name + '!')

    def attack(self, other):
        self.speak()
        print(self.name, 'used', self.basic_attack, '!')
        other.receive_damage(self.damage)
        if random() < self.prob and type(other) != ElectricType:
            other.paralyzed = True
        print(other.name, 'is paralyzed!')

    def receive_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
            print(self.name, 'fainted!')
