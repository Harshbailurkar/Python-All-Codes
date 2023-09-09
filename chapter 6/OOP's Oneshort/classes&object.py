class person:
    name="harsh"
    occupation="software engineer"
    networt=1000000
    def info(self):
        print(f"{self.name} is a {self.occupation}")
# self parameter is a reference to the current instance of class and 
# is used to access variable that belongs to the class
a=person()
print(type(a))
b=person()
c=person()
a.name="Harsh Bailurkar"
b.name="nikita"
b.occupation="HR"
print(a.name,"\t",a.occupation)
a.info()
b.info()
c.info()