#unit 8
#session 1
#ver 1
#prob 9

# Time - O(logn)
# Space - O(logn)
class TreeNode():
   def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

def find_bst(root, value):
  if not root:
    return False

  if root.val == value:
    return True

  elif root.val > value:
    return find_bst(root.left, value)

  else:
    return find_bst(root.right, value)

root = TreeNode(1, TreeNode(2, TreeNode(5)), TreeNode(3))
print(find_bst(root, 3)) #true
print(find_bst(root, 8)) # false
