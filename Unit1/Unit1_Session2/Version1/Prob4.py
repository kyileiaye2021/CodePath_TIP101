#unit 1
#Session 2
#VEr 1
#Problem 4

#create a func with a list as a param
#create a new list to store the modified ele in the orig list
#using for loop, put each modified ele in the new list 
#return the new list

def flip_sign(lst):
  new_list = []
  for ele in lst:
    new_list.append(ele * -1)

  return new_list

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)