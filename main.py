def two_sum(nums, target):
  l, r = 0, len(nums) -1
  target_sum_index_lst = []

  while l < r:
    addition = nums[l] + nums[r]
    if addition > target:
      r -= 1
    elif addition < target:
      l += 1
    else:
      target_sum_index_lst.append(l)
      target_sum_index_lst.append(r)
      return target_sum_index_lst

nums = [2,7,11,15]
sol1 = two_sum(nums, 9)
print(sol1)
sol2 = two_sum(nums, 18)
print(sol2)
