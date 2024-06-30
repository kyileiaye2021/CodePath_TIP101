def min_merge_operations(nums):
  left, right = 0, len(nums) - 1
  total_count = 0

  while left < right:
    if nums[left] == nums[right]:
      right -= 1

    else:
      nums[left + 1] += nums[left]
      total_count += 1
    left += 1

  return total_count

nums = [6,1,3,7]
print(min_merge_operations(nums))

nums2 = [1,3,3,1]
print(min_merge_operations(nums2))

nums3 = [1,3,2,7]
print(min_merge_operations(nums3))