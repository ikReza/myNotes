class User():
    def sign_in(self):
        print("logged in!")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f"{self.name} is attacking with power of {self.power}")
        
# introspection
wizard1 = Wizard("Valhala", "charm")
wizard1.attack()

# get the available method/attributes -> introspect
print(dir(wizard1))
"""
We'll see so many unknown dunders/magic methods
"""

# Dunders/Magic methods
