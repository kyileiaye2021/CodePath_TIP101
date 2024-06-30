#unit 4
#session 2
#ver 2
#prob 3

# create two pointers 0 and 1
# iterative over the list untill even and odd index reaches the nums lst end
#   iterate until the even index points to odd var
#   iterate until the odd index points to even var
#   if both even and odd index are not out of range
#      swap two var

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