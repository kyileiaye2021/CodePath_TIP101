#Unit 8
#session 1
#ver 3
#prob 8

# time - O(n)
# space - O(n)
class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right

def contains_greater(root, value):

  if not root:
    return False

  if root.val > value:
    return True

  return contains_greater(root.left, value) or contains_greater(root.right, value)

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(contains_greater(root, 6)) #False
print(contains_greater(root, 0)) #True

