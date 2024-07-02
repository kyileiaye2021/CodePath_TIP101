def sorted_squares(nums):
  squared_lst = [0] * len(nums)
  left, right = 0, len(nums) - 1
  for i in range(len(nums)-1, -1, -1):
    if abs(nums[left]) > abs(nums[right]):
      square = nums[left] ** 2
      left += 1
    else:
      square = nums[right] ** 2
      right -= 1
    squared_lst[i] = square
  return squared_lst

nums = [1,2,3,4]
sq_nums = sorted_squares(nums)
print(sq_nums)
nums2 = [-4,-1,0,3,10]
sq_nums2 = sorted_squares(nums2)
print(sq_nums2)
