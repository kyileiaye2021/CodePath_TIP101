#unit1
#session2
#ver2
#problem 3

#create a func with a list as a param
#create a new list
#itereate over each ele in the orig list and increment it by 1
#put it in the new list
#return list

def increment_values(lst):
  new_lst = []
  for ele in lst:
    new_lst.append(ele + 1)

  return new_lst

lst = [3,5,8,2]
new_lst = increment_values(lst)
print(new_lst)