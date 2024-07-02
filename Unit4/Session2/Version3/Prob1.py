#unit 4
#session 2
#ver 3
#prob 1

# * Two pointer approach with a new list
# * create two pointers pointing to the index 0 of lst1 and lst2
# * create a new list to store the ele in sorted order
# * iterate until lst1 index and lst2 index reaches their ends
#   * if the lst1 index var is the same as lst2 index var,
#      * increment both pointers by 1
#   * otherwise
#      * if lst1 index var is less than lst2 index var
#        * increment lst1 index by 1
#      * otherwise, 
#        * increment lst2 index by 1
# * return the sorted list

def find_intersection(lst1, lst2):
  lst1_index = 0
  lst2_index = 0
  merged_sorted = []
  while lst1_index < len(lst1) and lst2_index < len(lst2):
    if lst1[lst1_index] == lst2[lst2_index]:
      merged_sorted.append(lst1[lst1_index])
      lst1_index += 1
      lst2_index += 1

    else:
      if lst1[lst1_index] < lst2[lst2_index]:
        lst1_index += 1
      else:
        lst2_index += 1

  return merged_sorted

  
lst1 = [1,2,4,6,7]
lst2 = [2,3,4,7]
print(find_intersection(lst1, lst2)) #[2,4,7]