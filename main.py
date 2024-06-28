def removeElement(nums, val):
  unique_index = 0

  for i, num in enumerate(nums):
    if num != val:
      nums[unique_index] = num
      unique_index += 1

  del nums[unique_index:]
  return len(nums)

nums = [5, 4, 4, 3, 4, 1]
nums_len = removeElement(nums, 4)
print(nums) # same list
print(nums_len)