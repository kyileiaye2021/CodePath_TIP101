#unit 10
#session 1
#ver 3
#prob 4

# Assumption
# if the tree has no node or only one node, output - 0

'''Happy case'''
#     1
#    /  \
#   2    3
#  /
# 4

#output - 3

'''Edge case'''
# input - 1
# output - 0

# input - None
# output - 0

# DFS
# check if the current node is none
#    return 0
# recursively call on left subtree 
# recursively call on right subtree
# get the value of subtree that has max height 
# return 1 + max_height val

class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def dfs(root, max_length):

  if not root:
    return 0

  left_height = dfs(root.left, max_length)
  right_height = dfs(root.right, max_length)
  max_length[0] = max(max_length[0], (left_height + right_height) )
  return 1 + max(left_height, right_height)


def get_diameter(root):
  max_length = [0]
  dfs(root, max_length)
  return max_length[0]

root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(get_diameter(root)) #3

root = TreeNode(1)
print(get_diameter(root)) #0

root = None
print(get_diameter(root)) #0

root = TreeNode(1, TreeNode(2))
print(get_diameter(root)) # 1