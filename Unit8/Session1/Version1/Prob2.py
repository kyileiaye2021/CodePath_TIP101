#unit 8
#session 1
#ver 1
#prob 2

class TreeNode:
  def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def check_tree(root):
  return root.val == root.left.val + root.right.val

root = TreeNode(10)
left_child = TreeNode(4)
right_child = TreeNode(6)
root.left = left_child
root.right = right_child
print(check_tree(root))