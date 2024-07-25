#Unit 8
#session 1
#ver 2
#prob 2

class TreeNode:
  def __init__(self, value, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def check_tree(node):
  return (node.val == (node.left.val * node.right.val))

root = TreeNode(10)
left_child = TreeNode(2)
right_child = TreeNode(5)
root.left = left_child
root.right = right_child

print(check_tree(root))