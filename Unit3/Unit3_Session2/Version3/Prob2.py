#unit 3
#session 2
#version 3
#prob 2

#edge cases
#nums = None, output = None
#nums = [], output = 1
#nums = [1], output = 2
#nums = [1,1], output = 2
#nums = [1,2,3,4], output = 5
#nums = [1,2,3,5,6,10], output = 4

#High Level Plan
#*Iterative approach
    #iterate over the list and find the diffference between the curr ele and the prev ele
    
#Low level plan
#iterate over the nums list
    #find the difference between curr ele and prev ele
    #if the difference is greater than 1
        #return prev ele + 1


def find_missing_positive(nums):
  if len(nums) == 0:
    return 1
  if len(nums) == 1:
    return 2

  res = 0
  for i in range(1, len(nums)):
    diff = nums[i] - nums[i-1]
    if diff > 1:
      return nums[i-1] + 1
    else:
      res = nums[i]

  return (res + 1)
  
nums1 = [1,2,3,5,6,10]
print(find_missing_positive(nums1)) #4

nums2 = [1,2,3,4,5]
print(find_missing_positive(nums2)) #6

nums3 = []
print(find_missing_positive(nums3)) #1

nums4 = [1]
print(find_missing_positive(nums4)) #2

nums5 = [1,1]
print(find_missing_positive(nums5)) #2
 