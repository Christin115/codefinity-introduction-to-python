# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"
candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[22:27]
category1 = categories[0:11]
category2 = categories[13:24]
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

print(f"we have {candy1.lower()} for {bubblegum_price} in the {category1.lower()}")
print(f"we have {candy2.lower()} for {chocolate_price} in the {category1.lower()}")
print(f"we have {dry_goods.lower()} for {pasta_price} in the {category2.lower()}")
