#unit 6
#session 2
#ver 2
#prob 6


#Edge Cases
#lst1 = None, lst2 = None, output = []
#lst1 = None, lst2 = {1,2,3}, output = {1,2,3}
#lst1 = {1,2,3}, lst2 = None, output = {1,2,3}
#lst1 = [], lst2=[] , output = []
#lst1 = [1,2,3], lst2 = [], output = [1,2,3]
#lst1 = [], lst2 = [1,2,3], output = [1,2,3]
#lst1 = [1,2,3,4], lst2 = [10,20],output = [1,10,2,20,3,4]
#lst1 = [10,20], lst2 = [1,2,3,4], output = [10,1,20,2,3,4]

#High Level Plan
#Iterative Approach
  #iterate over the lst1
      #add ele of lst1 in odd index
      #add ele of lst2 in even index
  #if there are remaining ele in the lst2, append those ele in the list

#Low Level Plan
#create a new list
#iterate over the lst1
  #if curr index % 2 != 0:
      #add the ele of lst1 to the lst
  #else: add the ele of lst2 to the lst

#count how many ele are still left in the lst2
#iterate over the lst2 that amount of times
    #append the remaining ele in the list


def interleave_lists(lst1, lst2):
  if not lst1 and not lst2:
    return []

  if not lst1 and lst2:
    return lst2

  if not lst2 and lst1:
    return lst1

  lst1_index = 0
  lst2_index = 0
  new_lst = []
  for i in range(len(lst1)):
    if i % 2 == 0:
      new_lst.append(lst1[lst1_index])
      lst1_index += 1

    else:
      new_lst.append(lst2[lst2_index])
      lst2_index += 1

  #adding remaining ele
  if len(lst2) > len(lst1):
    for i in range(lst2_index, len(lst2)):
      new_lst.append(lst2[i])

  else:
    for i in range(lst1_index, len(lst1)):
      new_lst.append(lst1[i])


  return new_lst

lst1 = [1, 2, 3, 4]
lst2 = [10, 20]
lst3 = []
inter_lst = interleave_lists(lst1, lst2)
print(inter_lst) #[1,10,2,20,3,4]
inter_lst1 = interleave_lists(lst2, lst3)
print(inter_lst1) #[10,20]
inter_lst2 = interleave_lists(lst3, lst2)
print(inter_lst2) #[10,20]
inter_lst3 = interleave_lists(None, None)
print(inter_lst3) #[]
inter_lst4 = interleave_lists(lst2,None)
print(inter_lst4) #[10,20]
inter_lst5 = interleave_lists(None, lst2)
print(inter_lst5) #[10,20]
inter_lst6 = interleave_lists([], [])
print(inter_lst6) #[]