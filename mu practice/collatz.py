# Write your code here :-)


def collatz(number):


    try:
        number = int(number)
        if(number%2) == 0:
            print(number//2)
            return number//2




        else:
            print(3*number+1)
            return 3*number+1


    except:
        print('Not an integer')
        return 1


while True:
    print('Enter a number')
    start = input()

    while True:
        if start == 1:
            break

        else:
            start = collatz(start)


