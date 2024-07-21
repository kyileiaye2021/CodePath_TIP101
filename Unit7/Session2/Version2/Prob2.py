#unit 7
#session 2
#ver 2
#prob 2

# The list is soreted
# contains only 0s and 1s
# must be solved in O(logn)

# is it possible that the list is empty or null? -> return 0
# [0,0,1,1] -> 2
# [0] -> 1
# [] -> 0

# High Level Plan
# * iterative approach : time - O(n)
# * binary search approach: time - O(log(n))

# Low Level Plan
# * create two pointers low pointing to 0 and high pointing to last indesx
# * iterate thru list until low passes high
#   * find the mid
#   * check if the mid ele is 0 
#     * shift the left pointer to mid + 1
#   * check if the mid ele is greater than 0
#     * shift the right pointer to mid - 1
# return the (right + 1)

# Implement the code

def count_zeros(lst):
  left, right = 0, len(lst) - 1
  while left <= right:
    mid = (left + right) // 2

    if lst[mid] > 0:
      right = mid - 1

    else:
      left = mid + 1

  return (right + 1) 

# Example Input: [0, 0, 0, 0, 1, 1, 1]
lst = [0,0,0,0,1,1]
print(count_zeros(lst)) #4

lst2 = [0,0,1,1] 
print(count_zeros(lst2)) #2

lst3 = [0]
print(count_zeros(lst3)) #1

lst4 = []
print(count_zeros(lst4)) #0

#Time complexity : O(logn)
#Space complexity: O(1)