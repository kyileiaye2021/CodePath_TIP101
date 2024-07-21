#unit 7 
#session 2
#ver 3
#prob 3

def binary_search_recursive(arr, target, left, right):
  if left > right and left < len(arr):
    return left

  if left > right and left >= len(arr):
    return -1
    
  mid = (left + right) // 2

  if target > arr[mid]:
    return binary_search_recursive(arr, target, mid + 1, right)
  else:
    return binary_search_recursive(arr, target, left, mid - 1)

def binary_search(lst, target):
  return binary_search_recursive(lst, target, 0, len(lst) - 1)
  
lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 4
print(binary_search(lst, target)) #2

lst2 = [1,2,3,5,6]
target2 = 20
print(binary_search(lst2, target2)) #-1
# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 20, left = 0, right = len(lst) - 1
# Expected Output: -1
# Explanation: 20 is not in the list