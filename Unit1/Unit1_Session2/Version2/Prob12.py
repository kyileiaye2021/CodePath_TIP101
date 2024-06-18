#unit 1
#session 2
#ver 2
#problem 12

#create a func with a list and a target val as params
#create a new list to store the indices of where the target found
#create a var to store the index num
#use for loop to iterate over the list and check the target is found
#if found, append it to the new list
#return new list

def find_all_occurrences(lst, target):
  new_list = []
  index_num = 0
  for ele in lst:
    if target == ele:
      new_list.append(index_num)
    index_num += 1
  return new_list

lst = [1,2,6,5,2,1,3,2,2]
index_list = find_all_occurrences(lst, 2)
print(index_list)