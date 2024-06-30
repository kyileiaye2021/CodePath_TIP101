def find_largest_k(nums):
  pos_index = -1
  neg_index = -1

  for i, ele in enumerate(nums):
    if ele < 0:
      if (neg_index < 0) or (neg_index >= 0 and ele < nums[neg_index]):
        neg_index = i

    else:
      if (pos_index < 0) or (pos_index >= 0 and ele > nums[pos_index]):
        pos_index = i
        
  smallest_ele = nums[neg_index] * -1
  largest_ele = nums[pos_index]
  if smallest_ele == largest_ele:
    return smallest_ele
  else:
    return -1

nums = [-1,2,-3,3,-1]
print(find_largest_k(nums))

nums2 = [-10,2,7,-3]
print(find_largest_k(nums2))