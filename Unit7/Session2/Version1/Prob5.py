#unit 7
#session 2
#ver 1
#prob 5

#Merge Sort (O(nlogn)) | Divide and Conquer Approach
# 

# Helper function: Merges two sorted lists into one sorted list
def merge(left, right):
  result = [] # List to store the merged result
  i = j = 0 # Pointers to iterate over left and right input arrays

  # Compare elements from left and right halves of the list and add them to the
  # result list in the correct order
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
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

