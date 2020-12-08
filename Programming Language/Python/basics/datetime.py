# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 10:28:56 2020

@author: ikr
"""

import datetime as dt

today = dt.date.today()
print(today)

print(f"Day -> {today.day}")
print(f"Weekday -> {today.weekday()}")
#Monday = 0, Sunday = 6

birthday = dt.date(1995, 7, 24)
print(birthday)

print(f"Age: {(today-birthday).days}")

#Datetime.date(Y, M, D)
#Datetime.time(h, m, s, ms)
#Datetime.datetime(Y, M, D, h, m, s, ms)