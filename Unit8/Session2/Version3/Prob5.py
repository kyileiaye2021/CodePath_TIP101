#Unit 8
#session 2
#ver 3
#prob 5

# BST find floor
# Time complexity - O(n)
# Space complexity - O(1)

class TreeNode:
  def __init__(self, value, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def find_floor(root, value):
  floor_val = None

  while root:
    if root.val == value:
      return root.val

    elif floor_val <= root.val:
      root = root.right

    else:
      root = root.left

  return floor_val





