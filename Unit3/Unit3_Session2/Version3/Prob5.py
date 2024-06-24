#unit 3
#session 2
#version 3
#prob 5

'''
Key Takeaways
pop(i) func remove the ele that the index i is pointing to 
so, move all next ele to the left by 1
'''
#Edge Cases
# lst1 = [], lst2 = [], output = None
# lst1 = [], lst2 = [1,2], output = None
# lst1 = [1,2], lst2 = [], output = None
# lst1 = [1,2], lst2 = [1,2], output = []
# lst1 = [3,1,8,10], lst2 = [4,5,3,7,8], output = [1,10,4,5,7]

#High Level Plan
# *Brute Force 
    #create a new list
    # iterate over one of the list and in each iteartion , check if the curr ele isn't  in another list, append ele in new lst
# *Iterative Approach
    #iterate thru the shorter list
    #check if the curr ele is in another lst, remove that ele from both lsts
    #combine those two list and return


#Low Level Plan
#check the lengths of the lists to get the shorter list
#iterative over the shorter list
  #if curr ele is in another lst
    #remove the ele from both of the lists
#combine the two list
#return the combined list

def exclusive_elements(lst1, lst2):
  if len(lst1) == 0 or len(lst2) == 0:
    return None

  temp_list = []
  list_to_search = []

  if len(lst1) > len(lst2):
    temp_list = lst2
    list_to_search = lst1
  else:
    temp_list = lst1
    list_to_search = lst2

  i = 0
  while i < len(temp_list):
    if temp_list[i] in list_to_search:
      list_to_search.remove(temp_list[i])
      temp_list.pop(i)
    i += 1

  return (temp_list + list_to_search)

lst1 = [3,1,8,10]
lst2 = [4,5,3,7,8]
lst3 = []
excl_lst = exclusive_elements(lst1, lst2) #[1,10,4,5,7]
excl_lst2 = exclusive_elements(lst1, lst1) #[]
excl_lst3 = exclusive_elements(lst3, lst2) #None
print(excl_lst)
print(excl_lst2)
print(excl_lst3)