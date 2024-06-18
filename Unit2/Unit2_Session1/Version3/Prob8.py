#unit 2
#session 1
#ver 3
#prob 8

#create a dict
#iterate over list_a
#check the key of list_a is in list_b
#if it's , remove the key_val pair
#put the rest of items in list_a and list_b into the dict

def find_unique_items(list_a, list_b):

  result_dict = {}

  for ele in list_a:
    if ele not in list_b:
      result_dict[ele] = "True"

  for ele in list_b:
    if ele not in list_a:
      result_dict[ele] = "False"

  return result_dict

list_a = ["apple", "banana", "carrot"]
list_b = ["apple", "banana", "date"]
print(find_unique_items(list_a, list_b))