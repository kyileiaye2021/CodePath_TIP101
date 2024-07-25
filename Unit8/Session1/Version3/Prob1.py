#Unit 8
#session 1
#ver 3
#prob 1

class TreeNode:
  def __init__(self, value, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right


root = TreeNode('a')
left_child = TreeNode('b')
right_child = TreeNode('c')
right_grand_child = TreeNode('d')

root.left = left_child
root.right = right_child
right_child.right = right_grand_child