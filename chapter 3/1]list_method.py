l = [1, 3, 4, 5, 6, 7, 4]

l.append(1)  # add at end
print(l)

l.sort()   # sort the list
print(l)

l.sort(reverse=True)  # sort in desending order
print(l)

l.reverse()   # reverse the original list
print(l)

a = l.index(3)  # return index of element
print(a)

b = l.count(4)   # count the occurence
print(b)

m = l.copy()  # creat the copy of list and in this copy the changes are not affect the originak list
m[0] = 'a'
print(m, l)

l.insert(1, 543)  # insert the data 543 at 1st location
print(l)

p = [234, 32, 223, 21]
m.extend(p)      # join 2 list and creat the changes in list
print(m)

k = l+p     # join 2 list and creat new list
print(k)
