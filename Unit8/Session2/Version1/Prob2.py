#unit 8
#session 2
#version 1
# prob 2

# Time complexity - O(n)
# Space complexity - O(n)
class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right


def height(root):
  if not root:
    return 0
  left_height = height (root.left)
  right_height = height(root.right)
  return max(left_height, right_height) + 1

root = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1))
print(height(root)) # 3

root1 = TreeNode(4)
print(height(root1)) # 1