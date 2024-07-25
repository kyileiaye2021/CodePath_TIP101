#Unit 8
#session 1
#ver 3
#prob 5

class TreeNode:
  def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def left_most_iterative(root):
  lst = []
  curr_root = root
  while curr_root:
    lst.append(curr_root.val)
    curr_root = curr_root.left
  return lst

root = TreeNode(10)
left_child = TreeNode(4)
right_child = TreeNode(6)
left_grandchild = TreeNode(5)
root.left = left_child
left_child.left = left_grandchild
root.right = right_child
print(left_most_iterative(root))

