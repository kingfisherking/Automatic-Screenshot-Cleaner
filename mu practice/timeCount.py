# Write your code here :-)
import time

def timeCount():
    number = input()
    try:
        number = int(number)
    except:
        print('enter numbe rpls')
        timeCount()


    if number > 0:
        time.sleep(1)
        for count in range(number):
            print(number - (count+1))
            #number = number - count
            time.sleep(1)
        print("Enter new Number")
        timeCount()

timeCount()
