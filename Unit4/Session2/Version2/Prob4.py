#unit 4
#session 2
#ver 2
#prob 4

# Assumption
# nums cannot be empty or null
# The list can or cannot be panlindrome at the end

# Low Level Planning
# create two pointers 
# create total num of addition to get panlindrome
# iterate until the l pointer passes r poointer
#   if l var and r var are equal
#     move both pointers inward
#   else: add l var to l+1 var
#     increment the total num of addition
#  return total num

def min_merge_operations(nums):
  left, right = 0, len(nums) - 1
  total_count = 0
  
  while left < right:
    if nums[left] == nums[right]:
      right -= 1
      
    else:
      nums[left + 1] += nums[left]
      total_count += 1
    left += 1

  return total_count
  
nums = [6,1,3,7]
print(min_merge_operations(nums))

nums2 = [1,3,3,1]
print(min_merge_operations(nums2))

nums3 = [1,3,2,7]
print(min_merge_operations(nums3))