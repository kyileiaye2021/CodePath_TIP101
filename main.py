def sort_array_by_parity(nums):
  even = 0
  odd = 1
  while even < len(nums) and odd < len(nums):
    while even < len(nums) and nums[even] % 2 == 0:
      even += 2
    while odd < len(nums) and nums[odd] % 2 == 1:
      odd += 2

    if even < len(nums) and odd < len(nums):
      temp = nums[even]
      nums[even] = nums[odd]
      nums[odd] = temp
  return nums
nums = [4,2,5,7]
nums2 = [2,3]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))