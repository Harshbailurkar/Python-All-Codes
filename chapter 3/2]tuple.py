# tuples are unchangeable
# to change the tuple convert it into list
# eg
tup = (1,)  # must need , if only 1 element is present
print(tup[0])

countries = ("spain", "italy", "india", "england", "germany")

if "india" in countries:
    print("yahhoooo!!!")

tup1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
tup2 = tup1[1:4]
print(tup2)
