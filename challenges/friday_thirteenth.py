# Write a function to detect 13th Friday. The function 
# can accept two parameters, and both will be numbers. 
# The first parameter will be the number indicating the 
# month, and the second will be the year in four digits. 
# Your function should parse the parameters, and it must 
# return True when the month contains a Friday with the 13th, 
# else return False.

from datetime import datetime

def has_friday_thirteenth(month, year):
    day = datetime(year, month, 13)

    if day.weekday() == 4:
        return True
    else:
        return False