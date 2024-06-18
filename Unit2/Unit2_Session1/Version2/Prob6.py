#unit 2
#session 1
#ver2 
#prob 6

#create a list
#iterate over the products dict
#compare the value of each key with restock_threshold
#if it's less than threshold, put the key in the list
#return the list

def get_items_to_restock(products, restock_threshold):
  product_list = []
  for key in products:
    if products[key] < restock_threshold:
      product_list.append(key)

  return product_list

products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5
print(get_items_to_restock(products, restock_threshold))