#unit 1
#session 2
#Ver 1
#PRoblem 7

#create a func with a lst (int type) as a para
#create a new list to store the even ele in the orig list
#in each iteration, use modulus operator to get remainder 0 to get even numbers
#store that current ele in th new lst
#return the new created list

def get_evens(lst):
  new_lst = []
  for ele in lst:
    if ele % 2 == 0:
      new_lst.append(ele)

  return new_lst

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)