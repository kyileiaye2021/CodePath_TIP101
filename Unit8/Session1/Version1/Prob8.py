#unit 8
#session 1
#ver 1
#prob 8

# Find the node in the tree
# time: O(n)
# space: O(n)
class TreeNode():
   def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

def find(root, value):
  if not root:
    return False

  if root.val == value: # if the value is found
    return True
  else:

    checkleft = find(root.left, value) # check the left subtree
    if not checkleft: # check right subtree if not found in left subtree
      checkright = find(root.right, value)
      return checkright
    else:
      return checkleft

root = TreeNode(1, TreeNode(2, TreeNode(5)), TreeNode(3))
print(find(root, 3))
print(find(root, 8))