#unit 2
#session 2
#ver 1
#prob 2

#create a new dict
#iterate over the dict1
#if key in the dict2, put it in the new dict

def common_keys(dict1, dict2):
  common_lst = []
  for key in dict1:
    if key in dict2:
      common_lst.append(key)
  return common_lst

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)