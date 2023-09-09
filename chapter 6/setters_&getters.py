
class myclass:

    def __init__(self,value):
        self.__value= value

    def show(self):
        print(f"value is { self.__value}")
    
    @property
    def value(self):                         # getter
        return 10*self.__value

    @value.setter
    def value(self,new_value):
        self.__value= new_value+10

obj= myclass(10)
print(obj.value)
obj.value= 20
print(obj.value)



