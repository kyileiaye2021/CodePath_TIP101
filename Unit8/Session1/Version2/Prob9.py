#Unit 8
#session 1
#ver 2
#prob 9

class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right

def is_leaf_bst(root, value):
  if not root:
    return False
  if (not root.left or not root.right) and root.val == value:
    return True

  elif root.val > value:
    return is_leaf_bst(root.left, value)

  else:
    return is_leaf_bst(root.right, value)

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
value = 5
print(is_leaf_bst(root, value)) #true
print(is_leaf_bst(root, 6)) #false