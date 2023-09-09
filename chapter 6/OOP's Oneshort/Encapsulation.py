# to retrict user to overwrite attribute

import csv


class Item:
    pay_rate = 0.8
    all = []

    # write the data type, it gives us mandaty to enter the correct data
    def __init__(self, name: str, price: float, quantity=0):
        # float recives both int value and float
       # Run validations to the received arguments

        assert price >= 0, f"price {price} is not valid"
        assert quantity >= 0, f"price {quantity} is not valid"

       # assign to self object
        # add __(double underscore for read only "@property" only in class
        self.__name = name
        # level outside class just nuse name without __)
        self.__price = price
        self.quantity = quantity

        # Action to execution

        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    @ property
    # property decorator = read-only Attribute
    def name(self):                     # name is read only
        print("hello")
        return self.__name

# first commend this and run program and the uncomment it and run
# this setter decoratoe allow to overwrite a value
    @name.setter
    def name(self, value):
        print("you are trying to set")
        if len(value) > 10:
            raise Exception("the name is too long")
        self.__name = value

    def calculate_total_price(self):
        return self.__price*self.quantity

    def discount(self):
        self.__price = self.__price * self.pay_rate
        # self.price = self.price * .pay_rate
        return self.__price

    def increment(self, incre):
        if self.price<0:
            raise Exception("prise should be greater than 0")
        self.__price = self.__price + self.__price*incre

    @classmethod  # decorator
    def instantiate_from_csv(cls):    # takes class as parameter instend of self
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):  # here give parameter as normal function

        # we will count out the floats that are point zero i.e: 5.0,10.0

        if isinstance(num, float):   # isinstance() is buitin function
            # it check the num is float no or not

            # count out the float that are point zero
            return num.is_integer()  # is_interger() is build-in function which checks the num is
            # interger or not and return boolean value i.e. true or false
            # if num= float then it will return false

        elif isinstance(num, int):
            return True

        else:
            #   return False
            pass

    def __repr__(self):

        return f"{self.__class__.__name__}('{self.name}',{self.__price},{self.quantity})"


item1 = Item("harsh", 10, 2)
print(item1.name)
print(item1.price)
# item1.read_only_name ="bbb"
item1.name = "bbb"

# item1.price=9
# item1.name="bbbpwjbhgcfsjhjh"
item1.increment(0.2)      #use increment or discount fun to change the value
print(item1.name)
print(item1.price)
