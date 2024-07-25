#Unit 8
#session 1
#ver 3
#prob 4

class TreeNode:
  def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def left_most_recursive(root):
  lst = []
  if not root:
    return lst
  lst.append(root.val)
  return lst + left_most_recursive(root.left)

root = TreeNode(10)
left_child = TreeNode(4)
right_child = TreeNode(6)
left_grandchild = TreeNode(5)
root.left = left_child
left_child.left = left_grandchild
root.right = right_child
print(left_most_recursive(root))


