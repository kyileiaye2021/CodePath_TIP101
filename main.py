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

