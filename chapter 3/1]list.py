# lists are order collection of data structure
# list are changable

l = [3, 4, 5, 2, 3, 7, 5, 7]
print(l)
print(type(l))

print(l[0], l[2])

print(l[-1])  # for -ve indexing index=len(list/string)-1

print(l[:])
print(l[1:])
print(l[1:5])
print(l[1:-1])
print(l[0:6:2])  # jumping index

list = ["red", "blue", "green"]
print("\"", list[0], list[2], list[1], "\"")

if "blue" in list:    # same thing applied to the string
    print(" yes ")
else:
    print("no")


# List comprehention

lst = [i*i for i in range(4)]
print(lst)

lst1 = [i*i for i in range(4) if i % 2 != 0]
print(lst1)
