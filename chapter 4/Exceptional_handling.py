try:
    a = int(input("enter the number"))  # here give input  as a string
    print(f"the multiplication table of {a} is: ")
    for i in range(1, 11):
        x = a*i
        print(a, "x", i, "=", x)

    b = [6, 3, 8]
    print(f"the value at index {a} is ", b[a])
except ValueError:

    print("invalid input !!!! ✋✋\n plz give right input ")

except IndexError:

    print("table of ", a, " is done but,\n index error")


print("submit the reponce")
