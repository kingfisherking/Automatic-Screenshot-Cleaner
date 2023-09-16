#! python 3
#regexStrip.py - a regex focused version of the strip method

import re


stripRegex = re.compile(r'(\S)')

test = 'hello world'

stripList = stripRegex.findall(test)

stripped = ''

for x in stripList:
    stripped = stripped + x

print(stripped)

