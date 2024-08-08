#unit 10
#session 1
#ver 2
#prob 4

# Sum Tree

# Edge Cases:
# input - None, output - True
# input - Node(1), output - True

# Happy Cases:
#    14
#    / \
#   4   6
#  / \
# 3   1
# Input: root = 14
# Expected Output: True (4+3+1+6 = 14)

# Plan
# DFS 
# helper func (total_sum , root)
# if the curr node is a leaf node, return root.val
# total_sum += left sub tree sum + right sub tree sum

# main func (root)
# if not root, return False
# if not root.left and not root.right, return True
# total_children_sum = 0
# call helper func
# check the root val is the same as total_children_sum
#   return true

# Implement
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def dfs(root):
  if not root:
    return 0
  return root.val + dfs(root.left) + dfs(root.right)

def check_root_sum(root):
  if not root:
    return True

  left_subtree = dfs(root.left)
  right_subtree = dfs(root.right)
  return root.val == (left_subtree + right_subtree)

root = TreeNode(14, TreeNode(4, TreeNode(3), TreeNode(1)), TreeNode(6))
print(check_root_sum(root)) #true


