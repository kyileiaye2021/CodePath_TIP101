def remove_duplicates(nums):
  a = 1
  b = 1

  while a < len(nums):
    if nums[a] != nums[a - 1]:
      nums[b] = nums[a]
      b += 1
    a += 1

  del nums[b:] #this doesn't create O(n) 

nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list

nums1 = [1]
print(nums1)
print(remove_duplicates(nums1))
print(nums1)