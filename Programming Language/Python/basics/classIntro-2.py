# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 18:53:25 2020

@author: Ibrahim Kaiser
"""

class Person:
    #constructor: __init__ -> short form of initialize
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print("Hello!")
        
    def greet(self):
        print(f"Hi! I'm {self.name}. Nice to meet you.")
        
        
kitty = Person("Kitty Schrodinger")
kitty.talk()
print( kitty.name)

smith = Person("William Smith")
smith.greet()