#unit 10
#session 2
#ver 2
#prob 5

'''Happy case'''
# in - [1,8,6,2,5,4,8,3,7], out - 49

'''Edge case'''
# in - [], out - 0
# in - [1], out - 0
# in - [1,1], out - 1

# Two pointer approach
# create two pointers pointing to start and end of the array
# create a var tostore max area
# iterate until left passes right
#   find curr area
#   update the max area if curr area is greater than max area
#  move pointer that points to the short line 

def max_area(height):
  if len(height) < 2:
    return 0

  left, right = 0, len(height) - 1
  max_area = float('-inf')

  while left < right:
    curr_area = (right - left) * min(height[left], height[right])
    max_area = max(max_area, curr_area)

    if height[left] < height[right]:
      left += 1
    else:
      right -= 1

  return max_area

lst = [1,8,6,2,5,4,8,3,7]
print(max_area(lst)) #49

lst = []
print(max_area(lst)) # 0

lst = [1, 1]
print(max_area(lst)) #1



