#unit 8
#session 1
#ver 1
#prob 4

class TreeNode:
  def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def left_most(root):
  if not root.left:
    return root.val
  return left_most(root.left)

root = TreeNode(10)
left_child = TreeNode(4)
right_child = TreeNode(6)
left_grandchild = TreeNode(5)
root.left = left_child
root.left.left = left_grandchild
root.right = right_child
print(left_most(root))
