# write a python program to translate a message into secrete code language. use the rules given
# below to translate normal english into secreat code language

''' encoading:
            if the word contains at least 3 characters , remove the first letter and append it
    at the end. now append three random character at the starting and end
    else :
        simply reverse the string
        
    Decoding:
             if the word contain less 3 char. reverse it
             else:
                remove 3 random character from start and end. now remove the last letter and
 
                append it to start '''


def encode():
    str = input("enter the sentance :")
    if (len(str) == 1 or len(str) == 2):
        print(str[::-1])
    else:
        first = str[0]
        str = str[1:]
        random = ""
        for i in range(3, 9):
            if (i % 2 != 0):
                random += str[i]

        str = random+str+first+random
        print(str)


def decode():
    str = input("enter the sentance :")
    if (len(str) == 1 or len(str) == 2):
        print(str[::-1])
    else:
        str = str[3:(len(str)-3)]
        last = str[-1]
        str = str[:-1]
        str = last+str
        print(str)


try:
    ask = 0
    while (ask != 2):
        ask = int(input(
            "what do you want to do? press 1 for encoding 0 for decoding and press 2 to exit? "))
        match ask:
            case 1:
                encode()
            case 0:
                decode()
            case 2:
                exit()

            case _:
                print("invalid input !! 🤦‍♂️🤦‍♀️")


except ValueError:
    print("invalid input !! 🤦‍♂️🤦‍♀️\t plz Try again \n plz enter 1 for encoding and 0 for decoding!!!  ")
