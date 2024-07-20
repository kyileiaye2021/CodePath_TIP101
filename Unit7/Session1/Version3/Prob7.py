#unit 7
#session 1
#ver 3
#prob 7

# x = 8 -> 2
# x = 4 -> 2
# x = 0 -> 0
# x = 1 -> 1
# x = -2 -> none

# two pointer technique | binary search
# create left and right pointers to 1 and (x//2)
# itereate the loop until the left passes right
#    get mid ele
#    check the square of mid ele is equal to x
#      return the mid ele
#    if the square of mid ele is less than x
#      shift left to mid + 1
#    else:
#      shift right to mid - 1
# return right

def sqrt(x):
  if x < 2:
    return x
  low, high = 1, (x//2)
  while low <= high:
    mid = (low + high) // 2
    mid_squared = mid * mid

    if mid_squared == x:
      return mid

    elif mid_squared < x:
      low = mid + 1

    else:
      high = mid - 1

  return high

print(sqrt(8)) #2
print(sqrt(16)) #4
print(sqrt(1))
