class empoyee:
    def __init__(self, name=str,id=int) :
        self.__name=name
  
    
e=empoyee("harsh",2010)

#print(a.__name) gives error
print(e._empoyee__name)