#Unit 8
#session 1
#ver 3
#prob 3

class TreeNode:
  def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def check_tree(root):
  if not root:
    return False

  if not root.left or not root.right:
    return False

  return (root.left.val == root.right.val)

root = TreeNode(1)
left_child = TreeNode(2)
right_child = TreeNode(2)
root.left = left_child
root.right = right_child
print(check_tree(root))