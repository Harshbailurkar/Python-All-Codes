# printing the hello world
print("hello world")
# -------------------------------------------------------------------------------------------------------------------
# to new line use "\n"
print("my name is Harsh\ni am form ajara")
# -----------------------------------------------------------------------------------------------------------------
# Escape sequence character
# it is \ followed by the character you want to insert eg. if we want to "some word" in print function it will
# generate error so we use this
# print("my name is "harsh" and i am from ajara") this will generate error
print("my name is \"harsh\" and i am from ajara")

print("hey", 6, 7)
# --------------------------------------------------------------------------------------------------------------------

# sep separeate the words defaultly it is sapce. end = print the this in the last of printing satatment
print("hey", 6, 7, sep="~", end="009\n")

# -------------------------------------------------------------------------------------------------------------------------------
# data types :-
'''
a= 1 - int ; b= true - boolean ; c="harsh - string ; d = none - none type ;
'''
a = 2
b = "harsh"
c = 3
d = complex(2, 3)  # represent complex no 2 + 3i
print(a, b)
print(a+c)
# to find out type of any datatype use type() fuction
print("the type of a and d is ", type(a), type(d))
# ----------------------------------------------------------------------------------------------------------------

# operators
'''
+ - * / % '''
print(a+c)
print(a-c)
print(a*c)
print(a/c)
print(a//c)  # floor div
print(a % c)
print(a**c)  # exponential

# is and ==
z = 2
p = "2"
q = [1, 2, 3]
r = [1, 2, 3]
f = (9, 8)
g = (9, 8)
o = 1
i = 1
print(z is p)  # compaire exact location in memory
print(z == p)  # compaire values
print(q is r)
print(q == r)
# return both true as tuple is immutable and 1 is constant
print(f is g)
print(f == g)
print(o is i)
print(o == i)
# ----------------------------------------------------------------------------------------

# typecasting :
# it is used to change the type of variable[ int() , ord(),tuple(), set(),list(),dict(),float() ]
a = "2"
b = "23"
print(int(a)+int(b))
