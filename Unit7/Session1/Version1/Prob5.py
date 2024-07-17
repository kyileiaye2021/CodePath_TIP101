#unit 7
#session 1
#ver 1
#prob 5

def binary_search(lst, target):
  left = 0
  right = len(lst) - 1

  while left < right:
    # Find the middle index of the array
    mid = (left + right) // 2

    # If the value at the middle index is the target value:
    if lst[mid] == target:
      # Return the middle index
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


lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print(binary_search(lst, target))
# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
# Expected Output: 5
# Explanation: 11 has index 5 in the list
