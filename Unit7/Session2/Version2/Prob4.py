#unit 7
#session 2
#ver 2
#prob 4

# Is it possible that the list is empty or null? (return -1)
# Any constraint for time and space complexitiees? 
# Are there any repetitive nums in the list? (yes)

'''
Assumption
The list can be null or empty
The list is sorted
The ele does not have to be in the lst
'''

# Test cases
# Happy cases
# [3,5,5] -> 2
# [0,3,4,5] -> 3
# [4,4,5,8] -> 3

# Edge cases
# [] -> -1
# [0,0,0] -> -1


# High Level Plan
# * Iterative Approach: Time- O(n), Space - O(1)
# * Binary Search Approach: check the first index is 
def is_special(nums):
  pass