
class Item:
    

    @staticmethod              
    def is_integer(num):  # here give parameter as normal function 

           #we will count out the floats that are point zero i.e: 5.0,10.0
           
           if isinstance(num,float):   # isinstance() is buitin function 
                                       # it check the num is float no or not

              #count out the float that are point zero
              return num.is_integer() #is_interger() is build-in function which checks the num is 
                                    #interger or not and return boolean value i.e. true or false
                                    # if num= float then it will return false       
                                                           
           elif isinstance(num,int):
              return True
              
           else:
            #   return False
             pass


print(Item.is_integer(7))
print(Item.is_integer(7.0))
print(Item.is_integer(7.5))