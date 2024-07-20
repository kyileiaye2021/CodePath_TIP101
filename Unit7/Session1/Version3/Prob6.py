#unit 7
#session 1
#ver 3
#prob 6

'''
mid index in the binary search is less than mid element then 
there is a missing num in the first half of the lst.

no repetitive num in the lst
so every ele should match the index in the list


'''

# Time complexity of O(logn)
# create two pointers
# iterate until the left pointer passes right
#  find mid index
#  check if the mid index is less than mid ele (there is a missing num in first half)
#    shift the right pointer 
#  otherwise, shift the left 

# 1, 2, 3, 4, 5 -> 0
# 0, 1, 3, 4, 5 -> 2
# 0, 1, 2, 4 -> 3
# 0, 2, 3, 4 -> 1
def find_missing(nums):
  if not nums:
    return -1

  left = 0
  right = len(nums) - 1
  
  while left <= right:
    mid = (left + right) // 2

    if mid <= nums[mid]:
      right = mid - 1
    else:
      left = mid + 1

  if left >= len(nums):
    return left
  return left - 1

lst = [1,2,3,4,5] 
find_missing(lst) #0
lst2 = [0,1,3,4,5] 
find_missing(lst2) #2
lst3 = [0,1,2,4]
find_missing(lst3) #3
lst4 = [0,2,3,4]
find_missing(lst4) #1
lst5 = [0]
find_missing(lst5) #1




