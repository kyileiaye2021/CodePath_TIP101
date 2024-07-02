#unit 4
#session 2
#ver 3
#prob 2

'''
Sorting the list is the key here. If the left end + right end < target, left end + other var less than right end is also < target.
'''
# * TWO POINTER APPROACH  
# sort the list in ascending order
# * create two pointers pointing to index 0 and last index
# * create a var to store the total num of count
# * iterate over the list until left passes right
#    * check left var + right var < target
#      * count = right index - left index
#      * move left to right by 1
#    * move right to left by 1
# * return the total count
def count_pairs(nums, target):
  nums.sort()
  left, right = 0, len(nums) -1
  total_count = 0
  while left < right:
    if nums[left] + nums[right] < target:
      total_count += (right - left)
      left += 1
    else:
      right -= 1
      
  return total_count

nums = [-1,1,2,3,1]
print(count_pairs(nums,2))

nums2 = [-6,2,5,-2,-7,-1,3]
print(count_pairs(nums2,-2))