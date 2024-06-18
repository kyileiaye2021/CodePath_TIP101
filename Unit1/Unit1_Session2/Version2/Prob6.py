#unit 1
#session 2
#ver 2
#problem 6

#create a func with a list as a param
#create a new list
#use range func and step back by 1 from the end for each iteration
#put that current ele in the new list
#return the new list
'''
def reverse_list(lst):
  new_list = []
  index = len(lst) - 1
  while index >= 0:
    new_list.append(lst[index])
    index -= 1

  return new_list
'''
##we can also use insert() and add every ele at the beginning of the list
def reverse_list(lst):
  new_list = []
  for i in range(len(lst)-1, -1, -1):
    new_list.append(lst[i])

  return new_list

lst = [1,2,3,4,5]
rev_lst = reverse_list(lst)
print(rev_lst)



