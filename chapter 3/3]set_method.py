# to get union of set(combine 2 or more sets)
s1 = {1, 2, 3, 4, 5}
s2 = {5, 4, 6, 2, 3}
print(s1.union(s2))
print(s1)

# to update set
s1.update(s2)
print(s1, s2)

# intersection
a = {1, 2, 3, 4, 5, 7}
b = {5, 4, 6, 2, 3, 1}

k = a.intersection(b)
print(k)
s3 = a.intersection_update(b)  # gives comman values in 2 sets
print(s3)

#symantric difference: gives values which are not comman

print(a.symmetric_difference(b)) # A-B

#isdisjoint():
set={"mumbai",'pune','kolhapur','satara'}
set2={"sangali","mumbai",'pune','delhi','kolkata'}
set3={"mumbai","pune"}

print(set.isdisjoint(set2))   #show true if element does not match bet 2 sets

#issuperset

print(set.issuperset(set3))
print(set3.issubset(set))

#if you want to add single item in set use add()

set.add("kolkata")
print(set)

# to remove the values from set use remove()

set2.remove("kolkata")
print(set2)

#pop() remove random value which is actuallay last valus but differ each time as it is set

item=set.pop()
print(item,set)
# del s3 to delete entire set

# to delete all element in set use clear()
set3.clear()
print(set3)

#if else in set

if "mumbai" in set:
    print("mumbai is present")
else:
    print("mumbai is not present")