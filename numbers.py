# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import calendar
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
year=int(input("Years->"))
mon=int(input("Month->"))
date=int(input("Date->"))
print(days[calendar.weekday(year,mon,date)])
input("Press any key to continue...")