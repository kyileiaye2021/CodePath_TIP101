#get_first()
#a func with a list parameter 
#returns the first element of the list
#returns None if the list is empty

def get_first(lst):
  if len(lst) == 0:
    return None
  else:
    return lst[0]

print(get_first([3,1,6,7,5]))