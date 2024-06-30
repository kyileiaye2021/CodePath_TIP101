#unit 4
#session 2
#ver 2
#prob 2

'''
Sorting both lists in ascending order is key for correctly matching the smallest available cookie that can satisfy a child's greed.
'''
# Assumption
# Both the lst cannot be null or empty
# The size of the s and g may or may not be the same
# the size of the g must be less or equal to that of s

# High Level Planning
# * Iterative Approach
#   * iterate over g and for each ele in g, compare it with curr ele in the list s and return the num of content children
# * Two pointer approach
#   * create two pointers pointing to the index 0 of both list. then iterate over the list and check the g[i] == s[j]
#   * create a var and increment that var everytime there is a content child

# Low Level Planning
# * Two Pointer Approach
# * return False if the size of g is greater than that of s
# * create var to store the num of content children 
# * create two pointers to keep track of the list index of g and s
# * iterate over g and s
#   * if g[i] <= s[j]
#      * increment the var by 1
#   * increment i and j by 1
# * return the var

def find_content_children(s, g):
  if len(g) > len(s):
    return False

  g.sort()
  s.sort()

  i, j = 0, 0
  num_of_content_children = 0
  while i < len(g) and j < len(s):
    if g[i] <= s[j]:
      num_of_content_children += 1
    i += 1
    j += 1

  return num_of_content_children

g = [1,2,3]
s = [1,1,3]
# There are 3 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 1 --> content child

# child `1` has a greed factor of 2
# cookie `1` has a size of 1, this child will not be content

# child `2` has a greed factor of 3
# cookie `2` has a size of 3 --> content child

print(find_content_children(s, g))
# Output: 2 

g = [1,1]
s = [2,2,2]
# There are 2 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 2 --> content child

# child `1` has a greed factor of 1
# cookie `1` has a size of 1 --> content child

print(find_content_children(s, g))
# Output: 2 