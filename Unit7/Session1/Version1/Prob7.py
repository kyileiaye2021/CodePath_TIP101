#unit 7
#session 1
#ver 1
#prob 7

#find the floor 
# [1, 2, 8, 10, 11, 12, 19], x = 5 -> 2
# [1], x = 0 -> -1
# [], x = 5 -> -1

# Two pointer technique
# search using binary search algo
# if the target val is less than mid ele
#  shift the right pointer
# else:
#  assign the res to the curr mid index
#  shift the left pointer

def find_floor(lst, x):
  result = -1
  if not lst:
    return result
  left, right = 0, len(lst)
  while left <= right:
    mid = (left + right) // 2

    if x < lst[mid]:
      right = mid - 1

    else: 
      result = lst[mid]
      left = mid + 1

  return result

lst = [1,2,8,10,11,12,19]
x = 5
print(find_floor(lst, x))
lst2 = [1]
x2 = 0
print(find_floor(lst2,x2))
lst3 = []
x3 = 5
print(find_floor(lst3, x3))