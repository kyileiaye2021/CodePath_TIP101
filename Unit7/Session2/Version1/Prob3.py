#unit 7
#session 2
#ver 1
#prob 3

# [1, 2, 3], target = 3 -> 2
def binary_search(nums, target):
  return binary_search_recursive(nums, 0, len(nums) - 1, target)

def binary_search_recursive(nums, left, right, target):

  if left > right:
    return -1

  mid = (left + right) // 2

  if target == nums[mid]:
    return mid
  elif target > nums[mid]:
    return binary_search_recursive(nums, mid + 1, right, target)
  else:
    return binary_search_recursive(nums, left, mid - 1, target)


lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print(binary_search(lst, target))
# Example Input: nums = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
# Expected Output: 5
# Explanation: 11 has index 5 in the list