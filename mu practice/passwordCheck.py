#! python 3
#passwordCheck.py - checks to make sure that a password is at least 8 characters, contains upper/lower, and 1 digit

import re

def passwordCheck(password):
    strong = True

    upperRegex = re.compile(r'[A-Z]')
    lowerRegex = re.compile(r'[a-z]')
    digitRegex = re.compile(r'\d')

    check1 = upperRegex.search(str(password))
    check2 = lowerRegex.search(str(password))
    check3 = digitRegex.search(str(password))

    if len(password) < 8:
        strong = False
    if check1 == None:
        strong = False
    if check2 == None:
        strong = False
    if check3 == None:
        strong = False

    if strong == True:
        print("password strong: " + str(password))
    else:
        print("password weak: " + str(password))


passwordCheck('hello')
passwordCheck('Hello123')
