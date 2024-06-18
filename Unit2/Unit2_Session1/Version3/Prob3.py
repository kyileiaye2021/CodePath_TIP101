#Unit 2
#session 1
#ver 3
#prob 3

#create a bool var to keep track that the item is in the record or not
#iterate over the records dict
#check the current key is equal to the item
#update the value of the key 
#print out if it's not

def update_or_warn(records, item, update_value):
  is_exist = False
  for record in records:
    if record == item:
      records[item] = update_value
      is_exist = True

  if not is_exist:
    print(f"{item} not found")
    return
  else:
    return records


records = {"apple": 1, "banana": 2, "orange": 3}
print(update_or_warn(records, "banana", 5))

update_or_warn(records, "grape", 4)