#unit 7
#session 1
#ver 1
#prob 6

#Time complexity: O(n*m)
#space complexity: O(1)
def binary_search(lst, target):
  left = 0
  right = len(lst) - 1

  while left < right:
    # Find the middle index of the array
    mid = (left + right) // 2

    # If the value at the middle index is the target value:
    if lst[mid] == target:
      # Return the middle index
      while lst[mid] != target:
        mid += 1 
      return mid
    # Else if the value at the middle index is less than our target value:
    elif lst[mid] < target:
      # Update pointer(s) to only search right half of the list in next loop iteration
      left = mid + 1
    # Else
    else:
      # Update pointer(s) to only search left half of the list in next loop iteration
      right = mid - 1

  # If we search whole list and haven't found target value, return -1
  return -1

lst = [1, 3, 5, 7, 9, 11, 11, 13, 15]
target = 11
print(binary_search(lst, target)) #6
# Example Input: lst = [1, 3, 5, 7, 9, 11, 11 13, 15], target = 11
