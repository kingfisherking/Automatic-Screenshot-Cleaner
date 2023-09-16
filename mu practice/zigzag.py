# Write your code here :-)
import time, sys
indent = 0 #number of indents
indentIncreasing = True #whether or not indentation is increasing

try:
    while True: #main loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) #pause for 1/10 of a second


        if indentIncreasing:
            #increase number of spaces
            indent = indent + 1
            if indent == 20:
                #start decreasing indents
                indentIncreasing = False


        else:
            #decrease number of spaces
            indent = indent - 1
            if indent == 0:
                #start increasing again
                indentIncreasing = True


except KeyboardInterrupt:
    sys.exit()
