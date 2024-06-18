#unit1
#session2
#ver1
#problem 11

#create a func with a list as a para
#range() to iterate over the list
#print out the index of the list

def print_indices(lst):
  #range func can only accept the int type (not list)
  for i in range(len(lst)):
    print(i)

lst = [5,1,3,8,2]
print_indices(lst)