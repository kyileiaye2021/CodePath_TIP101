#Unit 8
#session 1
#ver 2
#prob 1

class TreeNode:
  def __init__(self, value, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right


root = TreeNode(5)
left_child = TreeNode(10)
right_child = TreeNode(20)