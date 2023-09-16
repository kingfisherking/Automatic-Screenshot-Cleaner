#! python3
#bulletPointAdder.py - Adds Wikipedia bullet points to the start
#of each line of text on the clipboard.

import pyperclip


text = pyperclip.paste()


lines = text.split('\n')
for i in range(len(lines)): #loop through all lines (indexes in wikipedia)
    lines[i] = '* ' + lines[i] #adds star/asterisk to line

text = '\n'.join(lines)




pyperclip.copy(text)
