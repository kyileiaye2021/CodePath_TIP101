#Last item

#a function with a list parameter and return an int if the list is not empty
#return None if the list is empty

def get_last(lst):
  if len(lst) == 0:
    return None
  else:
    return lst[len(lst) - 1]


print(get_last([3,1,6,7,5]))