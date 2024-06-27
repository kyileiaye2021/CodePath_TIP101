#unit 4
#session 1
#ver 1
#prob 4

def sort_array_by_parity(nums):
  a = 0
  b = len(nums) - 1
  while a < b:
    if nums[a] % 2 == 0:
      a += 1
    else:
      if nums[b] % 2 != 0:
        b -= 1
      else:
        temp = nums[a]
        nums[a]= nums[b]
        nums[b] = temp
        a += 1
        b -= 1

  return nums

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))