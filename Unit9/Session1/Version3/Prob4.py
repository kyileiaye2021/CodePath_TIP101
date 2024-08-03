#unit 9
#session 1
#ver 3
#prob 4


#   3 (root)
#  / \
# 9   20
#    /  \
#   15   7

# Helper func (root, left_height = 0, right_height = 0)
# base case:
# if the curr node is null, return True (balanced) and  0 (height)
# recursive case:
# call the recursive func on left subtree
# call the recursive func on right subtree
# update the balance of the current subtree
# update the height of the current subtree
# return balanced and height

# main func
# call recursive helper func
# return the balance

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def get_height(root):
  # base case
  if not root:
    return True, 0

  left_balanced, left_height = get_height(root.left)
  right_balanced, right_height = get_height(root.right)

  balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
  height = max(left_height, right_height) + 1

  return balanced, height

def is_balanced(root):
  balanced, height = get_height(root)
  return balanced

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(is_balanced(root)) # True

root1 = TreeNode(2)
print(is_balanced(root1)) #True

root2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
print(is_balanced(root2)) #False

# time complexity - O(n)
# space complexity - O(n)