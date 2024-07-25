#Unit 8
#session 1
#ver 2
#prob 8

# Binary Tree Is Leaf
# Time - O(n)
#Space - O(n)
'''
check the value is the same as the val of leaf node in the tree
'''

class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right

def is_leaf(root, value):
  if not root: # if no such value is found in the tree, return False
    return False
    
  if not root.left or not root.right and root.val == value:
      return True
  return is_leaf(root.left, value) or is_leaf(root.right, value)

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
value = 5
print(is_leaf(root, value))