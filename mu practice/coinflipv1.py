# This code checks whether or not a streak of 6 was achieved, but considers streaks above 6 as multiple streaks
#ie for streaks above 5 = n, the number of streaks is equal to streakNumber - n,  streak of 8 = 8-5 streaks, 3 streaks
import random

numberOfStreaks = 0

#0 is tails, 1 is heads
for experimentNumber in range(10000):
    coinFlipList = []

    for coinFlip in range(100):

        coinFlipList.append(random.randint(0, 1))

        if len(coinFlipList) > 6:
            testList = coinFlipList[len(coinFlipList)-6:len(coinFlipList)]
            if testList == [0]*6 or testList == [1]*6:
                numberOfStreaks += 1



print(numberOfStreaks)
print(numberOfStreaks / (100*10000))
