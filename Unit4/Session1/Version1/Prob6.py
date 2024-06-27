#unit 4
#session 1
#ver 1
#prob 6

# Can the list be null or empty? 

# Assumption
# list is sorted
# list cannot be null
# func return length of the modified list

# * High level planning
# * Brute Force
#    * create a new list. iterate over the list and add unique ele in the new list
# * Two Pointer 
#    * create two pointers starting from 1 because index 0 is always unique. 
#    * a will iterate thru the list to the end. b will only move if the unique ele is found
#    * delete the remaining ele in the list

# * Low Level Planning
# * create two pointers
# * first pointer will itereate unitl the end of the list
#    * if the unique ele is found
#      * unique ele will be assigned to the position where the b currently points to
#      * move the second pointer  by 1
#    * move the first pointer by 1
# * delete the remaining ele 
# * return the length of the list

def remove_duplicates(nums):
  a = 1
  b = 1

  while a < len(nums):
    if nums[a] != nums[a - 1]:
      nums[b] = nums[a]
      b += 1
    a += 1

  del nums[b:] #this doesn't create O(n) 

nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list

nums1 = [1]
print(nums1)
print(remove_duplicates(nums1))
print(nums1)