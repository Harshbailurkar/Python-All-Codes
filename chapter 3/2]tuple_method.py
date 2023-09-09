countries = ("spain", "italy", "india", "england", "germany")

temp = list(countries)
temp.append("russia")
temp.pop(3)
temp[1] = "finland"

countries = tuple(temp)
print(countries)

# concate the 2 tuple

countries1 = ("india", "afg", "pak")
countries2 = ("ban", "sl", "mal")

southasia = countries1+countries2
print(southasia)

# index of tuple

tuple1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple1.count(3))
b = tuple1.index(3)
# slice the tuple from 4 to 8 and give the index of element 5
c = tuple1.index(5, 4, 8)
print(b)
print(c)
print(len(tuple1))
