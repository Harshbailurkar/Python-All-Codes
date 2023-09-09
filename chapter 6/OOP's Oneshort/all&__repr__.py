class Item:
    
    pay_rate =0.8     # the pay rate after 20% discount [ apply discount to all object]
    all =[]   # all is list
    def __init__(self,name: str,price:float ,quantity=0):  # write the data type, it gives us mandaty to enter the correct data
                                                           # float recives both int value and float
       # Run validations to the received arguments

        assert price >=0,f"price {price} is not valid"
        assert quantity>=0,f"price {quantity} is not valid"

       # assign to self object
        self.name=name                                     
        self.price=price
        self.quantity=quantity

        #Action to execution

        Item.all.append(self)   #all is a list and we used append() function on list all which is in class Item

    
    def calculate_total_price(self):
            return self.price*self.quantity
    
    def discount(self):
        self.price= self.price * self.pay_rate
    
    def __repr__(self):  # to represention object in "all" list
        
         return f"Item('{self.name}',{self.price},{self.quantity})"

item1 = Item("phone",100,1)
item2 = Item("phone1",1000,3)
item3 = Item("phone2",10,5)
item4 = Item("phone3",50,5)
item5 = Item("phone4",75,5)

print(Item.all)    # because of Item.all.append(self) 

for i in Item.all:
    print(i.name)