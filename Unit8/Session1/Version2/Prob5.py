#Unit 8
#session 1
#ver 2
#prob 5

# Right most node (iterative)

class TreeNode:
  def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def right_most_iterative(root):
  curr_root = root
  while curr_root.right:
    curr_root = curr_root.right

  return curr_root.val

root = TreeNode(10)
left_child = TreeNode(4)
right_child = TreeNode(6)
right_grandchild = TreeNode(5)
root.left = left_child
root.right = right_child
right_child.right = right_grandchild
print(right_most_iterative(root))