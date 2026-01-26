# The item's discount and stock status have been defined
discounted = False
lowStock = True
movingProduct = (discounted == True) or (lowStock == True)
promotion = not movingProduct
print("Is the item eligible for promotion?", promotion)

