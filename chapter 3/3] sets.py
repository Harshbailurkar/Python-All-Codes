# sets are unordered collection of data, use curly braces, sets are unchangable.
# sets donot contain dublicate values and can not be access using index
s = {2, 3, 4, 6, 2, 6}
print(s)

info = {"harsh", 2, True, 6.8, "harsh"}
print(info)  # order will not be same as it does not maintain sequence

harsh = {}
print(type(harsh))  # the type will be dictinary

# to crreat empty set
a = set()
print(a)


#to traverse set use for loop

for i in info:
    print(i)