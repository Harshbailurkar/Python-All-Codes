# rock paper sissor game
# take input from user

# r= rock
# p =paper
# s=sissor

# computer     1   2   3
# user    s=1  D   w   l
#         w=2  l   D   w
#         g=3  w   l   D

import random

choise = 1
while (choise != 0):
    try:
        print(
            "\n\t Are you exited to play with computer? \n\t press 1 for sneck, 2 for water and 3 for gun: ")

        user = int(input(""))
        print("you: ", user)
        list = [1, 2, 3, 1, 3, 2, 3, 2, 1, 3, 1, 2, 2, 1, 3]

        computer = random.choice(list)
        print("computer: ", computer)

        if (user == computer):
            print("\tits a Draw !!!")

        elif ((user == 2 and computer == 3) or (user == 1 and computer == 2) or (user == 3 and computer == 1)):
            print("\t congratulation !!! its a win 🥳🥳😍 well plyed")

        elif (user <= 0 or user >= 4):
            print("\tinvalid input !!!! \n \t\t plz enter valid input")

        else:
            print("you lose 🫤🥲")

        choise = int(
            input("waana play again ??? if yes press any number or press 0 to exit "))
    except ValueError:
        print("invalid input !!!!")
