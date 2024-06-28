#unit 4
#session 1
#ver 2
#prob 6

# Assumption
# lst cannot be empty
# lst cannot be null
# there can be at least more than one val num in the lst

# High Level Planning
# * Iterative approach
#    * every time the val is found in the lst, remove it from the lst
# * Two pointer approach
#    * move every num except for val to the beginning of the lst
#    * delete the vals from the index after unique ele 

# Low Level Planning
# * create a unique index pointer pointing to index 0
# * iterate over the list 
#     * check if the curr ele isn't equal to val
#        * assign the curr ele to the index that the unique pointer index is currently pointing to
#        * move the unique index to right by 1
# delete the ele of the lst starting from the unique index to the end
# return the length of the list

def removeElement(nums, val):
  unique_index = 0
  
  for i, num in enumerate(nums):
    if num != val:
      nums[unique_index] = num
      unique_index += 1
      
  del nums[unique_index:]
  return len(nums)
  
nums = [5, 4, 4, 3, 4, 1]
nums_len = removeElement(nums, 4)
print(nums) # same list
print(nums_len)