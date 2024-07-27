# Problem 1
# check the val of every node is the same or not
# Traverse the left and right subtree 

# Test cases:
# root -> empty or there is only one node in the root, return false
# Example Input Tree #1

#       1
#      / \
#     /   \
#    1     1
#   / \     \
#  1   1     1

# Input: root = 1
# Expected Output: True

#Time Complexity - O(n)
#Space complexity - O(n)

class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right

def helper_univalued(root, var):
  if not root:
    return True

  if root.val == var:
    return helper_univalued(root.left, var) and helper_univalued(root.right, var)

  return False

def is_univalued(root):
  if not root:
    return False
  else:
    return helper_univalued(root, root.val)

root = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1))
print(is_univalued(root))# True

root2 = TreeNode(1, TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1))
print(is_univalued(root2)) # False

root3 = TreeNode(1)
print(is_univalued(root3)) #True
