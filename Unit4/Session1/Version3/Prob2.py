#unit 4
#session 1
#ver3
#prob 2

# Assumption
# list is sorted
# Every sum of two ele must be unique

# Hight level planning
# * Iterative Approach O(n^2)
# * Two pointer technique I
#   * create dict to store the ele and index 
#   * iterate over the list and subtract the curr ele from the target. find the diff in the dict and return index
# * Two pointer technique II
#   * itearte over the lst until l passes r
#   * shift the l and r around according to the addition

# Low level planning
# * create l and r 
# * create a list
# iterate over the list until l passes r
#    * find the addition of l and r
#    * check if the addition is greater than target
#        * move r to left by 1
#    * if the addition is less than the target
#        * move l to right by 1
#    *otherwise, add l and r to the list
# return the list

# Time complexity - O(n)
# Space complexity - O(1)

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
