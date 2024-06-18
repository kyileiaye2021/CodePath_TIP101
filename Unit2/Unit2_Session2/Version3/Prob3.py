def pop_stock(items, item_name, quantity):

  if item_name in items:
    if items[item_name] >= quantity:
      items[item_name] -= quantity
      return items
    else:
      return "Not enough stock"

  else:
    return "Item does not exist"

items = {"chocolate": 20, "candy": 5, "chips": 10}

resultA = pop_stock(items, "candy", 2)
resultB = pop_stock(items, "candy", 5)
resultC = pop_stock(items, "lollipops", 5)
resultD = pop_stock(items, "chocolate", 5)

print(resultA)
print(resultB)
print(resultC)
print(resultD)