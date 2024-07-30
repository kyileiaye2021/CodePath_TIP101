#Unit 8
#session 2
#ver 2
#prob 6

# Problem 6: Identical Binary Trees
#Time complexity - O(n)
#Space complexity - O(h) where h is the height of the smaller tree

class TreeNode():
  def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right


def is_identical(root1, root2):
  if not root1 and not root2:
    return True

  if not root1 or not root2:
    return False

  if root1.val != root2.val:
    return False

  return is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)

