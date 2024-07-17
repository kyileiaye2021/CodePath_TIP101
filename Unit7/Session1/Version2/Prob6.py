#unit 7
#session 1
#ver 2
#prob 6

# create left and right pointers
# in each iteration, compare the mid ele and x val
  # if mid ele is less than x val, shift left to mid + 1
  #else, result = mid
  # shift right to mid -1

def find_ceiling(lst, x):
  result = -1
  left = 0
  right = len(lst) - 1

  while left <= right:
    mid = (left + right) // 2

    if lst[mid] < x:
      left = mid + 1
    else:
      result = mid
      right = mid - 1

  return result
  
lst = [1, 2, 8, 10, 11, 12, 19]
print(find_ceiling(lst, 5))
lst2 = [2,3,4,5]
print(find_ceiling(lst2, 6))

# Example Input: lst = [1, 2, 8, 10, 11, 12, 19], x = 5
# Expected Output: 2
# 8 is the largest element in the list that is greater than or equal to 5. 
# 8 has index 2 in the list.

