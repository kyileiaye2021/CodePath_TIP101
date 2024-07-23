#unit 7
#session 2
#ver 1
#Prob 6

'''
Assumption:
All elements are unique
'''

'''
In this problem, we also need to check if the low ele is greater than or less than target to
know which part of the lst we need to search.
Also, we need to check if it is within the low and mid or the mid and high to shift around low and high pointers'''
# Two pointer approach | binary search algo
# create two pointers
# iterate until left passes right
#    find mid index
#    check if the mid ele is the same as the target
#      return mid index

#    check if the low ele is less than target
#      check if the target is between low and mid ele
#        shift right to left
#      otherwise, shift left to right

#    otherwise (low ele is greater than target ) 
#      check if the target is between mid and high ele
#        shift left to right
#      otherwise, shift right to left

#Time - O(logn)
#Space = O(1)
# Example Input: nums = [8, 9, 10, 2, 5, 6], target = 10
def search_circular_list(nums, target):
  low, high = 0, len(nums) - 1

  while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
      return mid

    elif nums[low] < target: #check if the target is between low and mid ele
      if nums[low] < target < nums[mid]:
        high = mid - 1
      else:
        low = mid + 1

    else: #if low ele is greater than target
      if nums[mid] < target < nums[high]:
        low = mid + 1
      else:
        high = mid - 1

  return -1

lst = [8, 9, 10, 2, 5, 6]
target = 10
print(search_circular_list(lst, target)) #2

lst2 = [9, 12, 15, 2, 5, 6, 8]
target2 = 5
print(search_circular_list(lst2, target2)) #4

lst3 = [9, 12, 15, 2, 5, 6, 8]
target3 = 7
print(search_circular_list(lst3, target3)) #-1