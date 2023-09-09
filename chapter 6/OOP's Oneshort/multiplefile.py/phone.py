from item import Item

class phone(Item):
   
    def __init__(self,name: str,price:float ,quantity=0, brokenphone=0):  # write the data type, it gives us mandaty to enter the correct data
        
       # Run validations to the received arguments
        
        assert brokenphone>=0,f"price {brokenphone} is not valid"
       # Call super function to have access to all attribute/ metods from parent class

        super().__init__(
            name,price,quantity
        )

       # assign to self object
        
        self.brokenphone=brokenphone
