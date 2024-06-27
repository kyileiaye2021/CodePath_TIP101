#unit 4
#session 1
#ver 1
#prob 4

'''
Even integers should be at the beginning of the list and odd ones should be at the end of the list.
So, create two pointers and check left pointer var points to even or odd.
If odd, swap it with the right one if the right one is even.
If the right one is also odd, find the even on the right side until even one's found
'''
#Problem 4: Move Even Integers
# Create two pointers
# one pointers to index 0 and another pointer points to last index
# iterate until the left pass the right
  # check the var pointed by left is even
      # move a to right by 1
  # otherwise
      # check the var pointed by b is even 
        # swap the ele and shift around both a and b
      #it is odd
        #move b to left by 1

def sort_array_by_parity(nums):
  a = 0
  b = len(nums) - 1
  while a < b:
    if nums[a] % 2 == 0: #check the left pointer var is even or odd
      a += 1
    else:
      if nums[b] % 2 == 0: #check the right pointer var is even or odd
        temp = nums[a]
        nums[a]= nums[b]
        nums[b] = temp
        a += 1
        
      b -= 1

  return nums

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))