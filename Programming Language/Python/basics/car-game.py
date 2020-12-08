# -*- coding: utf-8 -*-
"""
Spyder Editor

Car Game
"""
print("Car game starts. .. ...")
print("Type 'help' to see the keywords")

isStart = False
isStop = False

while True:
    key = input("> ").lower()
    if key == "help":
        print("start - to start your car")
        print("stop - to stop your car")
        print("quit - to quit the game")
    elif key == "start":
        print("Car starts moving") if(isStart == False) else print("Car is already moving")
        isStart = True
        isStop = False
    elif key == "stop":
        print("Stopping the car") if(isStop == False) else print("Car is already stopped")
        isStart = False
        isStop = True
    elif key == "quit":
        print("Closing the game")
        break
    else:
        print("Sorry! I don't understand your command")
