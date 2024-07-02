def count_pairs(nums, target):
  nums.sort()
  left, right = 0, len(nums) -1
  total_count = 0
  while left < right:
    if nums[left] + nums[right] < target:
      total_count += (right - left)
      left += 1
    else:
      right -= 1

  return total_count

nums = [-1,1,2,3,1]
print(count_pairs(nums,2))

nums2 = [-6,2,5,-2,-7,-1,3]
print(count_pairs(nums2,-2))