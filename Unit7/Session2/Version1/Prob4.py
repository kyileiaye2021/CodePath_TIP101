#unit 7
#session 2
#ver 1
#prob 4

# Is it possible that the array is not circular? [1]
# Is it possible that the array is empty or null?
# Can rotation be left rotation? (no) (only right rotation)
# Is it possible that the array is not rotated at all? 

'''
Assumption:
The integer list is sorted.
There are no duplicates in the list.
'''

# Happy cases
# [7,8,1,2,4,5] -> 2
# [4,5,6,2,3] -> 3

# Edge cases
# [1,2,5,6] -> 0 
# [2] -> 0
# [] -> 0

# High Level Plan 
# * Iterative Approach - Time: (O(n)) | Space: O(1)
# * Binary Search Approach with two pointers - Time: O(log n) | Space: O(1)

# Low Level Plan
# create two pointers
# iterate until left passes right
#   find the mid index
#   check if the next ele of mid index is less than the mid element
#      return (mid + 1)
#   if not, 
#      check if the prev ele of mid index is greater than the mid ele
#        return mid
#       else: shift the left to mid + 1
# return 0

def count_rotations(nums):
  left, right = 0, len(nums) - 1
  while left <= right:
    mid = (left + right) // 2

    if (mid + 1 < len(nums)) and nums[mid + 1] < nums[mid]:
      return (mid + 1)
    else:
      if nums[mid - 1] > nums[mid]:
        return (mid)
      else:
        left = mid + 1

  return 0

lst = [7,8,1,2,4,5]
print(count_rotations(lst)) #2

lst2 = [4,5,6,1,2,3]
print(count_rotations(lst2)) #3

lst3 = [1]
print(count_rotations(lst3)) #0

lst4 = []
print(count_rotations(lst4)) #0

lst5 = [2, 5, 6, 8, 11, 12, 15, 18]
print(count_rotations(lst5)) #0

lst6 = [11, 12, 15, 18, 2, 5, 6, 8]
print(count_rotations(lst6)) #4

