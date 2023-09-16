#! python 3
#dateDetection.py - detects valid dates within textinput

import re

dateRegex = re.compile(r'''(\d{2})\/(\d{2})\/(\d{4})''')
days30 = ['04', '06', '09', '11']
dateText = '06/23/1995'

dateSearch = dateRegex.search(dateText)

month = dateSearch.group(1)
day = dateSearch.group(2)
year = dateSearch.group(3)

validDate = True
leapYear = False

if int(year) % 4 == 0:
    leapYear = True
if int(year) % 100 == 0 and int(year) % 400 != 0:
    leapYear = False

if int(year) not in range(1000, 3000):
    validDate = False

if int(month) not in range(1,13):
    validDate = False

if month == '02':
    if int(day) not in range(1,29):
        validDate = False
    if day == '29' and leapYear == True:
        validDate = True

if month in days30:
    if int(month) not in range(1,31):
        validDate = False

if month not in days30:
    if int(month) not in range(1,32):
        validDate = False

print(dateText + ' is a valid date? ' + str(validDate))


