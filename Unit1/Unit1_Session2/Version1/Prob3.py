#Unit 1
#Session 2
#VEr 1
#Problem 3

#create a func called doubled()
#take a list as a param
#create a new list to store each doubled item in the list
#put each item in the new list using for loop
#return the new created list

def doubled(lst):
  new_lst = list()
  for ele in lst:
    new_lst.append(ele * 2)

  return new_lst

lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)