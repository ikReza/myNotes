class PlayerCharacter:
    # Class Object Attribute(static)
    membership = True
    def __init__(self, name="anonymous", age=0):
        self.name = name    #attributes(dynamic)
        self.age = age

    def run(self):
        print("run")
    
    def shout(self):
        print(f'my name is {self.name}')

player1 = PlayerCharacter("Reza", 25)
player2 = PlayerCharacter()

print(player1.name)
print(player2.age)
player1.run()
player2.shout()

# help(player1)  -> #shows blueprint