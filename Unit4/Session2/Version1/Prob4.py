#unit 4
#session 2
#ver 1
#Prob 4

# Assumption
# every ele in the list is not equal 0
# the list cannot be empty or null

# High Level Planning
# * Iterative Approach
#   * iterate over the list and find the max value. iterate thru the list again to find the neg pair of that num
# * Two pointer approach
#   * create two pointers. one pointing to the pos int index and the other one pointing to neg int index
#   * have to find the largest one of pos int val and neg pair

# Low level planning
# * create two pointers both pointing to 0
# * iterate over the list 
#   * if the curr ele is neg 
#     * if curr index == 0:
#        * assign the neg_pointer to that index
#     * if curr index > 0 and curr var < neg_pointer var
#        * neg pointer point to that one
#   * otherwise
#      * if cur index == 0:
#        * assign the pos_pointer to that index
#      * if curr index > 0 and curr var > pos pointer var
#        * pos pointer point to that one
#      
# * change the neg pointer val to pos val
# * check if that val equal to pos pointer val
#   * return pos pointer val
# * return -1

def find_largest_k(nums):
  pos_index = -1
  neg_index = -1

  for i, ele in enumerate(nums):
    if ele < 0:
      if (neg_index < 0) or (neg_index >= 0 and ele < nums[neg_index]):
        neg_index = i

    else:
      if (pos_index < 0) or (pos_index >= 0 and ele > nums[pos_index]):
        pos_index = i

  smallest_ele = nums[neg_index] * -1
  largest_ele = nums[pos_index]
  if smallest_ele == largest_ele:
    return smallest_ele
  else:
    return -1

nums = [-1,2,-3,3,-1]
print(find_largest_k(nums))

nums2 = [-10,2,7,-3]
print(find_largest_k(nums2))