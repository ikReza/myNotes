# OOP - Inheritance
# Wizard, Archer, Cavalry are the inherited/sub -/children/derived class of User

class User():
    def sign_in(self):
        print("logged in!")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f"attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f"attacking with arrows: Arrows left -> {self.num_arrows}")

class Cavalry(User):
    pass

wizard1 = Wizard("Beyonce", 50)
archer1 = Archer("Rey", 100)
cavalry1 = Cavalry()

"""
wizard1.sign_in()
wizard1.attack()

archer1.sign_in()
archer1.attack()

cavalry1.sign_in()
"""

# checking if the derived class is instance of a class
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, Archer))
# "object" is the base class of python
print(isinstance(wizard1, object))