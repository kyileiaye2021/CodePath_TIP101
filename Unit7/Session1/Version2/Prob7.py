#unit 7
#session 1
#ver 2
#prob 7


def ternary_search(lst, target):
  pass
  # Divide the array into three parts using two mid points (mid1 and mid2).
  low = 0
  mid1 = len(lst) // 3
  mid2 = mid1 * 2
  high = len(lst) - 1

  # While the lower bound is less than or equal to the upper bound:
  while low <= high:
    # Compare the target value with the values at mid1 and mid2:
    # If the target value matches mid1 or mid2
    if target == lst[mid1]:
      # the search is successful.
      return mid1
    elif target == lst[mid2]:
      return mid2
      
    # If the target is less than the value at mid1
    elif target < lst[mid1]:
      # search between the lower bound and mid1 - 1.
      high = mid1 - 1
      
    # If the target is between mid1 and mid2
    elif target > mid1 and target < mid2:
      # search between mid1 + 1 and mid2 - 1.
      low = mid1 + 1
      high = mid2 - 1
      
    # If the target is greater than the value at mid2
    else:
      # search between mid2 + 1 and the upper bound.
      low = mid2 + 1
      
  # Return -1, indicating the target is not in the array.
  return -1
  
# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print(ternary_search(lst, target))

target2 = 2
print(ternary_search(lst, target2))