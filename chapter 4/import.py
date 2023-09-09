import math

a=math.sqrt(9)
b=math.floor(4.3234)

print (a,b)

print("----------------------------------------------------------------------------------------------")

from math import sqrt,pi

c= sqrt(16)*pi
print(c)

print("----------------------------------------------------------------------------------------------")

# not recomented
from math import *
from math import sqrt,pi

d= sqrt(16)*pi
print(d)

print("----------------------------------------------------------------------------------------------")

from math import sqrt as s,pi

c= s(16)*pi
print(c)

print("----------------------------------------------------------------------------------------------")

print(dir(math))
print(math.nan,type(math.nan))

print("----------------------------------------------------------------------------------------------")
# costom import :  refer harsh.py file
from harsh import welcome,harsh

x=welcome()
z=print(harsh)

print(x,z)
