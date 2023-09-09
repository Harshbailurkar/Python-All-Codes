from item import Item

from phone import phone

Item.instantiate_from_csv()

print(Item.all)

item1 = Item("myitem", 700)
item1.name = "otheritem"
print(item1.name)
