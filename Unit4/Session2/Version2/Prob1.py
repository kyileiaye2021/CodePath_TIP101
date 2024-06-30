#unit 4
#session 2
#ver2 
#prob 1

# Assumption 
# lst1 and lst2 cannot be empty or null
# there can be repetitive nums in both lst

# Low level planning
# * Two Pointer Approach
# * create two pointers pointing to lst1 index and lst2 index
# * create a new list to store the vars
# * iterate over the lists until lst1 reaches its end and lst2 reaches its end
#   * compare lst1 curr var and lst2 curr var
#   * if lst1 curr var > lst2 curr var
#     * put that var in the list and increment lst1 index
#   * otherwise, 
#     * put that var in the list and increment lst2 index
# * return the new lst

def merge_sorted_lists(lst1, lst2):
  lst1_index = 0
  lst2_index = 0
  merged = []
  while lst1_index < len(lst1) and lst2_index < len(lst2):
    if lst1[lst1_index] < lst2[lst2_index]:
      merged.append(lst1[lst1_index])
      lst1_index += 1
    else:
      merged.append(lst2[lst2_index])
      lst2_index += 1

  while lst1_index < len(lst1):
    merged.append(lst1[lst1_index])
    lst1_index += 1

  while lst2_index < len(lst2):
    merged.append(lst2[lst2_index])
    lst2_index += 1

  return merged

lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
merged_lst = merge_sorted_lists(lst1, lst2)
print(merged_lst)

