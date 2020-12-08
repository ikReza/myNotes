# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 16:41:47 2020

@author: ikr
"""

print("Write your message: ")
message = input("> ")
words = message.split(" ")

#emoji in windows -> windows + .

emojis = {
    ":)": "😀",
    ":(": "😔",
    "xD": "😂",
    ":v": "🤣",
    ":'(": "😭"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
    
print(output)