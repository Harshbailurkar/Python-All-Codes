class person:
    def __init__(self, name, occupation):
        print("hey i am person")
        self.name = name
        self.occupation = occupation
    # name ="harsh"
    # occupation="developer"

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = person("harsh", "dev")
b = person("nikita", "HR")

a.info()
b.info()

# ------------------------------------------------------------------------------------


class Item:

    # the pay rate after 20% discount [ apply discount to all object]
    pay_rate = 0.8  # Global attributes [ class attribute]

    # write the data type, it gives us mandaty to enter the correct data
    def __init__(self, name: str, price: float, quantity=0):
        # float recives both int value and float
       # Run validations to the received arguments

        assert price >= 0, f"price {price} is not valid"  # exception line
        assert quantity >= 0, f"price {quantity} is not valid"

       # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity

    def discount(self):
        self.price = self.price * self.pay_rate
        #self.price = self.price * .pay_rate
        return self.price


item1 = Item("phone", 100, 5)
item2 = Item("laptop", 1000, 3)
# item3= Item("TV",-3,-1)
print(item1.calculate_total_price())
print(item2.calculate_total_price())

print(Item.pay_rate) # 0.8
print(item1.pay_rate) # 0.8   python will check "pay_rate" attribute at instance level and if it is not found then check at class level

print(Item.__dict__)  #  to see All the attributes for class level in dictinary format
print(item2.__dict__)  #  to see All the attribute for instance level

print(item1.discount())  
# or
print(item1.price)

item2.pay_rate = 0.7   # to apply discount to specific item

item2.discount()
print(item2.price)
