# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 09:32:40 2020

@author: ikr
"""

## Regular Expreesion - Regex

import re

##1
text = "A random string."
pattern = re.compile("A random string.")
result = pattern.search(text)
print(result)

##2
text = "B abc dkhj"
pattern = re.compile("[a-z]")
result = pattern.search(text)
print(result)

##3
text = "abc dkhj"
pattern = re.compile("[a-z]+")
result = pattern.search(text)
print(result)

##4
text = "abc134Dkhj"
pattern = re.compile("[a-z0-9]+")
result = pattern.search(text)
print(result)

##5
text = "abc134DEh j"
pattern = re.compile("[a-zA-Z0-9]+")
result = pattern.search(text)
print(result)

#### What can we do with this in our real life?

##Task-1: Find email id
email = "my address: MyId00@site.com. Feel free to contact me"
pattern = re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
result = pattern.search(email)
print(result)

##Task-2: Find multiple email id
email = "my primary id: MyId00@site.com, secondary id: Night@king.net"
pattern = re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
result = pattern.findall(email)
print(result)
