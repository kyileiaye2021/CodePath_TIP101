#unit 2
#session 1
#ver 3
#prob 2

#create a dict
#iterate over the list of the product_names
#assign key (product_name) and value(product_price) into dict
#return the dict

def build_inventory(product_names, product_prices):
  product_dict = {}
  for i in range(len(product_names)):
    product_dict[product_names[i]] = product_prices[i]

  return product_dict

product_names = ["Apple", "Banana", "Orange"]
product_prices = [0.99, 0.50, 0.75]
print(build_inventory(product_names, product_prices))