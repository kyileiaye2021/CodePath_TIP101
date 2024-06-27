def reverse_list(lst):
  # Create a new reversed list
  reversed_lst = lst[::-1]
  # Copy the elements back into the original list
  for i in range(len(lst)):
      lst[i] = reversed_lst[i]
  return lst

lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))