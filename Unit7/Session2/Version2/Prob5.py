#unit 7
#session 2
#ver 2
#prob 5

def merge_sort(arr):
  # If the length of the list is 0-1, the list is already sorted. 
  if len(arr) <= 1:
      return arr

  # Find the middle index of the array
  mid = len(arr) // 2
  # Divide the array into two halves
  left_half = arr[:mid]
  right_half = arr[mid:]

  # Recursive calls to merge_sort for sorting the left and right halves
  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)

  # Merge the sorted arrays
  return merge(left_half, right_half)

def merge(left, right):
  result = []
  i = 0
  j = 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1

    else:
      result.append(right[j])
      j += 1

  while i < len(left):
    result.append(left[i])
    i += 1

  while j < len(right):
    result.append(right[j])
    j += 1

  return result

lst = [1,5,8,2]
print(merge_sort(lst))

lst2 = [7,3,5,2,6]
print(merge_sort(lst2))