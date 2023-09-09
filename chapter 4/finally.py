try:
    l = [1, 2, 3, 2, 8, 9]
    i = int(input("enter the index: "))
    print(l[i])
except IndexError:
    print("limit exeed!!")

except ValueError:
    print("invalid input !!!")
finally:                            # it will always execued but the difference is
    print("i am alway execute\n\n")  # given in following example( in function)


# -------------------------------------------------------------------------------------

def fun():
    try:
        a = int(input("enter digit: "))
        if (a % 2 == 0):
            print("no is even")
        else:
            print("no is odd")
        return 1
    except ValueError:
        print("invalid input !!!!")
        print("enter valid input")
        return 0
    # print("the end")
    finally:
        print("the end")


fun()
