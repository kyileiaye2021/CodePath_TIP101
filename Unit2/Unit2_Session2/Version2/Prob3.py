#unit 2
#session 2
#ver 2
#prob 3

'''
If you remove things from a dict WHILE looping through the dict, your program will likely not work as intended.
'''
#create a list
#iterate over the dict
#if the item's price < price_threshold, add it to the lst
#if the lst is still empty, return None

def remove_items_below_price(items, price_threshold):
  lst = []
  for item in items:
    if items[item] < price_threshold:
      lst.append(item)

  if len(lst) == 0:
    return None

  else:
    for i in lst:
      if i in items:
        del items[i]
    return lst

items = {"apple": 1.99, "banana": 0.99, "cherry": 3.49, "date": 0.69}
removed_list = remove_items_below_price(items, 1.00)
print(removed_list)
removed_list_two = remove_items_below_price(items, 1.00)
print(removed_list_two)