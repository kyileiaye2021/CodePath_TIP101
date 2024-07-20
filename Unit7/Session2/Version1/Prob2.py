#unit 7
#session 2
#ver 1
#prob 2

# Two pointer technique (binary search)
# itereate until the low passes high
# find mid index
# check if the mid ele is less than 1
#   shift the left to mid + 1
# otherwise
#   shift the right to mid -1 
# At the end of the iteration, the left pointer will point to the start of the 1
# so return len(lst) - left

def count_ones(lst):

  left , right = 0, len(lst) - 1
  while left <= right:

    mid = (left + right) // 2
    if lst[mid] < 1:
      left = mid + 1

    else:
      right = mid - 1

  return len(lst) - left

print(count_ones([0, 0, 0, 0, 1, 1, 1]))#3
print(count_ones([0,0,1,1,1,1])) #4
