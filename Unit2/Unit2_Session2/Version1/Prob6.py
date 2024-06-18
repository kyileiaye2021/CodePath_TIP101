def hasDuplicates(nums, k):
  recent_index = {}
  for i in range(len(nums)):
      if nums[i] in recent_index:
          diff = i - recent_index[nums[i]]
          if diff <= k:
              return True
      recent_index[val] = i
  return False

nums = [5, 6, 8, 2, 4, 6, 9]
check1 = hasDuplicates(nums, 3)
print(check1)
check2 = hasDuplicates(nums, 4)
print(check2)