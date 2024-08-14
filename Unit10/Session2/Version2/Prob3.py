#Unit 10
#session 2
#ver 2
#prob 3

'''Happy CAse'''
# Input: heights = [4,3,2,1]
# Output: [0,1,2,3]

'''Edge Case'''
# Input : heights = [1,2,3,4]
# Output: [3]

# Input: heights = [2]
# Output : [0]

# Array Traversal
# create a list to store of indices of buildings
# create a max_height var to check the curr height is greater than the max_height
# iterate over the array from the right
#   check if the curr height is greater than max_height
#      append the index of curr height to the list
#      update the max_height
# reverse the list in ascending order
# return the list

def find_buildings(heights):
  res = []
  max_height = float('-inf')
  for i in range(len(heights) - 1, -1, -1):
    if heights[i] > max_height:
      res.append(i)
      max_height = max(max_height, heights[i])
  res.reverse()
  return res

heights = [4,2,3,1]
print(find_buildings(heights)) # [0,2,3]

heights = [1,2,3,4]
print(find_buildings(heights)) # [3]

heights = [2]
print(find_buildings(heights)) #[0]