#Unit 9
#session 1
#ver 1
#prob 5

# Helper func
# Base case:
 # if the curr node is none, return 0

# Recursive case:
 # return 1 + recursive call on left subtree + recursive call on right subtree

# Main func
# call the helper func to get the size
# check if the size is divisible by 2

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def get_size(root):
  if not root:
    return 0

  return 1 + get_size(root.left) + get_size(root.right)

def can_split(root):
  if not root:
    return False
  size = get_size(root)
  return size % 2 == 0

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(7)))
print(can_split(root)) # True

root2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(can_split(root2)) # False

# Time complexity - O(n)
# Space complexity - O(n)
