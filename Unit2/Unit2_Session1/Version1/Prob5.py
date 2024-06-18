def restock_inventory(current_inventory, restock_list):
  # compare the dictionaries
  for keys in restock_list.keys():
    if keys not in current_inventory.keys():
      current_inventory.update({keys: restock_list[keys]})

    else:#if the key already exists in the current_inventory
      current_inventory[keys] += restock_list[keys] #update the value
  return current_inventory


current_inventory = {
  "apples": 30,
  "bananas": 15,
  "oranges": 10
}

restock_list = {
  "oranges": 20,
  "apples": 10,
  "pears": 5
}

print(restock_inventory(current_inventory, restock_list))
'''
Output:
current_inventory = {
    "apples": 40,
    "bananas": 15,
    "oranges": 30,
    "pears": 5
}
'''