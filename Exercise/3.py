# koun baneka corer pati using list. i.e display questions

list1 = ["who is current PM of india ? \n [1] N. modi [2] M.sing [3] A.shah [4] N.Gadkari",
         "which is largest state in india (area wise)? \n [1] maharastra [2] utterpradesh [3] rajasthan [4]gujarat ",
         "how many contries are share borders with india? \n [1] 4 [2]5 [3]9 [4]7"]
list2 = ["1", "3", "4"]
a = 0

amount = 0

while (a == 0):
    for i in range(len(list1)):

        print(list1[i])
        uans = input("ans: ")

        if (list2[i] == uans):

            print("\ncongratulation 🥳🥳 !!! the ans is correct🙌👏👏")
            amount += 1000
            
            if (i < (len(list1)-1)):
                print("\nyou have now \"", amount, "\" Rs. in your wallet")

        elif (list1[i] != list2[i]):

            print("\nwronge ans!!! sry you are eliminated")
            amount = 0
            break

    print("\n")

    a += 1

if (amount == 3000):
    print("congrates!! 🥳🥳🥳 you won this game")

print("\n winning amount is:\"", amount+2000, "\" Rs.")
