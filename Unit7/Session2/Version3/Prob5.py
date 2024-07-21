#unit 7
#session 2
#ver 3
#prob 5

def merge(left, right):
  # Initialize an empty list to store the merged result
  result = []
  # Initialize a pointer to iterate over the left input list
  i = 0
  # Initialize a pointer to iterate over the right input list
  j = 0

  # Iterate over left & right lists simultaneously
  while i < len(left) and j < len(right):
    
    # Compare elements at same indices of left and right halves of the list 
    if left[i] <= right[j]:
    # Add them to the result list in the correct order
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
      
  # Add any remaining elements from the left half to the result list
  while i < len(left):
    result.append(left[i])
    i += 1
  # Add any remaining elements from the right half to the result list
  while j < len(right):
    result.append(right[j])
    j += 1

  return result

def merge_sort(lst):
  if len(lst) <= 1:
    return lst

  mid = len(lst) // 2
  left_half = lst[:mid]
  right_half = lst[mid:]

  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)

  return merge(left_half, right_half)

lst = [1,5,8,2]
print(merge_sort(lst))

lst2 = [7,3,5,2,6]
print(merge_sort(lst2))
    