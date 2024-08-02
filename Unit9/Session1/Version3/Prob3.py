#unit 9
#session 1
#ver 3
#prob 3

# Main Func 
# if the root is none, return False
# initialize a list to store the sum of all paths in the tree
# call helper func
# check if the target sum is in that list
#   return True
# return False

# Helper func
# if the curr node is none, return 0
# go to left subtree and update the left subtree
# visit right subtree and update the right subtree
# if the curr node is a leaf, append the sum value to the list

# Example Input Tree #1:

#       5
#      / \
#     4   8
#    /   / \  
#   11  13  4
#  / \       \
# 7   2       1

# Input: root = 5, target_sum = 22
# Expected Output: True
# Explanation: The root to leaf path 5 -> 4 -> 11 -> 2 sums to 22.

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def path_sum_helper(root, lst, sum):
  if not root:
    return 0

  sum += root.val
  if not root.left and not root.right:
    lst.append(sum)


  path_sum_helper(root.right, lst, sum)
  path_sum_helper(root.left, lst, sum)

def has_path_sum(root, target_sum):
  if not root:
    return False

  lst = []
  path_sum_helper(root, lst, sum = 0)

  for i in range(len(lst)):
    if lst[i] == target_sum:
        return True

  return False

root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
print(has_path_sum(root, 22)) # True

root2 = TreeNode(1, TreeNode(2), TreeNode(3))
print(has_path_sum(root2, 5)) # False