# treditinal method
def cube(x):
    return x*x*x

print(cube(2))

l=[1,2,3,4,5]
newl=[]
for item in l:
    newl.append(cube(item))

print(newl)

# map : it is higher order function i.e it takes function as argument

new2l=list(map(cube,l))
print(new2l)

new4l=list(map(lambda x: x*x*x*x,l))
print(new4l)

#Filter

def filter_function(a):
    return a>4

new3l=list(filter(filter_function,l)) # return true if a>4 and false if a<=4
print(new3l)

#reduce
from functools import reduce
sum= reduce(lambda x,y: x+y,l)  # first 1&2 reduce into 3,then the result & 3 is resuced 
                                 #and so on.here as the base case is addition hence add all no
print(sum)

