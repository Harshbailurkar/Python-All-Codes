class empoyee:
    def __init__(self, name=str,id=int) :
        self.name=name
        self.id=id
    def showdetails(self):
        print(f"the name of empoyee is {self.name} and the id is {self.id}")

class programmer(empoyee):
    def showlaguage(self):
        print("the defalut lag. is python")


e1=empoyee("harsh",1234)
e1.showdetails()

e2=programmer("harry",2343)
e2.showdetails()
e2.showlaguage()

#------------------------------------------------------------------------------------------------

