#Unit 9
#session 1
#ver 2
#prob 5

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def can_swap(root1, root2):
  if not root1 and not root2:
      return True
  if not root1 or not root2 or root1.val != root2.val:
      return False

  # Check if children are the same or swapped
  return (can_swap(root1.left, root2.left) and can_swap(root1.right, root2.right)) or \
    (can_swap(root1.left, root2.right) and can_swap(root1.right, root2.left))

def can_transform(root1, root2):
  return can_swap(root1, root2)

root1 = TreeNode(1, TreeNode(2))
root2 = TreeNode(1, None, TreeNode(2))
print(can_transform(root1, root2)) # FAlse

root3 = TreeNode(1, TreeNode(2), TreeNode(3))
root4 = TreeNode(1, TreeNode(3), TreeNode(2))
print(can_transform(root3, root4)) # True
