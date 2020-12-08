# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 16:57:38 2020

@author: Ibrahim Kaiser
"""

## Class Intro - 1

## Define class
class Point:
    #methods of object - move, draw
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
        
        
# create object
point1 = Point()
point1.draw()

point2 = Point()
point2.move()