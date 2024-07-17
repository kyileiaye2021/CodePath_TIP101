#unit 7
#session 1
#ver 2
#prob 5

# implement the iterative form of binary search algo
# in recursive form, it returns index val in each call of function
# if there is no value found, return -1 

# Recursive Approach
'''
Time Complexity: log(n) [func is called for half of the size of array ]
Space complexity: log(n) [the recursive depth being equal to the half of the size of array]
'''
def binary_search_recursive(arr, target, left, right):
  if left > right:
      return -1  # Base case: target not found within bounds

  # find middle index of list
  mid = (left + right) // 2

  # If the middle element is the target, return its index
  if arr[mid] == target:
      return mid
  # If the target is less than the middle element, search the left half
  elif arr[mid] > target:
      return binary_search_recursive(arr, target, left, mid - 1)
  # If the target is greater than the middle element, search the right half
  else:
      return binary_search_recursive(arr, target, mid + 1, right)


# Iterative Approach 
'''
Time Complexity: log(n) as we are using half of the array size everytime
Space Complexity: O(1) no space other than temp vars is created
'''
def binary_search_iterative(arr, target):
  left, right = 0, len(arr) - 1

  while left <= right:
    mid = (left + right) // 2
    
    if target > arr[mid]:
      left = mid + 1
    elif target < arr[mid]:
      right = mid - 1
    else: # if target == arr[mid]
      return mid
  return -1