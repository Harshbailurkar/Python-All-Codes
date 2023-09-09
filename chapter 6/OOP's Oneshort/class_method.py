
import csv


class Item:
    
    all =[]
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

        Item.all.append(self)

   
    
    @classmethod     #decorator
    def instantiate_from_csv(cls):    # takes class as parameter instend of self
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items=list(reader)

        for item in items:
            # print(item)   
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
                  
        
    def __repr__(self):
        
         return f"Item('{self.name}',{self.price},{self.quantity})"

Item.instantiate_from_csv()
print(Item.all)