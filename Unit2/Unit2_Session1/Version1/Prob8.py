#unit 2
#sesson 1
#ver 1
#problem 8

def index_to_value_map(lst):

  dict = {}
  for i in range(len(lst)):
    dict.update({i: lst[i]})

  return dict

lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))