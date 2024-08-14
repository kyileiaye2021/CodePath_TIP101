#unit 10
#session 2
#ver 1
#prob 4

'''Happy Case'''
# Input Tree #1:

#       3
#      /  \
#     9   20
#        /  \  
#       15   7

# Input: root = 3
# Output: True

# Input Tree #2:

#           1
#          / \
#         2   2
#        / \  
#       3   3
#      / \
#     4   4  

# Input: root = 1
# Output: False

'''Edge Case'''
# Input Tree #3: Empty Tree
# Input: root = 1
# Output: True

# DFS
# main 
# if there is only one node, return True
# if there is no node, return True
# initialize bool val
# call helper func
# return bool val

# helper (root, bool)
# if the curr node is none, return 0
# recursive call on left subtree
# recursive call on right subtree
# check if abs(left - right) > 1
# update bool val

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def dfs(root, check_bool):
  if not root:
    return 0

  left_height = dfs(root.left, check_bool)
  right_height = dfs(root.right, check_bool)

  if abs(left_height - right_height) > 1:
    check_bool[0] = False

  return 1 + max(left_height, right_height)


def is_balanced(root):
  if not root or not root.left and not root.right:
    return True

  check_bool = [True]
  dfs(root, check_bool)
  return check_bool[0]

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(is_balanced(root)) # True

root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
print(is_balanced(root)) # False

root = None
print(is_balanced(root)) #True
