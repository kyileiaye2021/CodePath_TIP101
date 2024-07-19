#unit 7
#session 1
#ver 3
#prob 5

def binary_search(lst, target):
  # Initialize a left pointer to the 0th index in the list
  left = 0
  # Initialize a right pointer to the last index in the list
  right = len(lst) - 1

  # While left pointer is less than right pointer:
  while left < right:
    # Find the middle index of the array
    mid = (left + right) / 2
    
    # If the middle value is the target value, return True
    if target == lst[mid]:
      return True
    # If the middle value is smaller than the target value, search the right half of the list
    elif target > lst[mid]:
      left = mid + 1
    # If the middle value is greater than the target value, search the left half of the list
    else:
      right = mid - 1
    
  # Return False if the target element has not been found
  return False

lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print(binary_search(lst, target))


# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
# Expected Output: True