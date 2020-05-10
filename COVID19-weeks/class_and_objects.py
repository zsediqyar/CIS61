from random import randint
# from math import gcd


''' OBJECTS 
    a metaphor for computation using distributed state
'''


class Rectangle:
    pass


a = Rectangle()
a.x = 5
a.y = 10

print(a)
print(a.x)
print(a.y)


class Rec:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def area(self):
        return self.x * self.y


r1 = Rec(5, 10)
r1.area()
print(r1.area())


class Account:
    max_withdrawal = 10

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        pass


alex = Account("Alex")
alex.holder
alex.balance
alex.balance = 100

tiff = Account("Tiffany")
tiff.balance = 50

'''SYNTAX OF A CLASS'''
'''
__init__ is a constructor in a class. 

'''

a = Account("Alex")
m = Account("Matt")
a.balance = 100
m.balance = 80
a.max_withdrawal
m.max_withdrawal
Account.max_withdrawal = 20
a.max_withdrawal
m.max_withdrawal

'''
getattr
hasattr

getattr(a, 'balance')
hasattr(a, 'balance')
'''


class Dice:
    # class attributes
    pass

    # constructor
    def __init__(self, sides=6):
        self.sides = sides
        self.face = 1

    # methods
    def roll(self):
        self.face = randint(1, self.sides)
        return self.face

    def get_face(self):
        return self.face


''' INHERITANCE '''
# Rational Class
# Attributes > numerator | denominator
# Methods > Print() | Add()


class Rational:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def print_rat(self):
        if self.denom == 1:
            print(self.numer)
        else:
            print(self.numer, "/", self.denom)


half = Rational(1, 2)
half.print_rat()

q = Rational(1, 4)
q.print_rat()

half2 = Rational(2, 4)
half2.print_rat()

whole = Rational(1, 1)
whole.print_rat()


class Pokemon:
    def __init__(self, name, trainer, level, hp, attack):
        self.name = name
        self.trainer = trainer
        self.level = level
        self.hp = hp
        self.attack = attack

    def print_poke(self):
        print("Name: ", self.name)
        print("Trainer: ", self.trainer)
        print("Level: ", self.level)
        print("HP: ", self.hp)
        print("Attack: ", self.attack)


poke = Pokemon("Zaki", "Lima", 5, 50, "Tackle")
poke.print_poke()


class Animal:
    pass


class Dog(Animal):
    pass


class Chicken(Animal):
    pass


class Labrador(Dog):
    pass
