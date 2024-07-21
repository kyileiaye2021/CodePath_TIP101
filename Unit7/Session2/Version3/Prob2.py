#unit 7
#session 2
#ver 2
#prob 2

def search_insert(nums, target):
  left, right = 0, len(nums) - 1

  while left <= right:
      mid = (left + right) // 2

      # Check if the middle element is the target
      if nums[mid] == target:
          return mid

      # If the target is less than the middle element, search in the left half
      if target < nums[mid]:
          right = mid - 1
      # Otherwise, search in the right half
      else:
          left = mid + 1

  # If the target is not found, 'left' will be the index where it can be inserted.
  return left

