#Unit 9
#session 1
# ver 1
#prob 1

# Problem 1: Is Symmetric Tree

# Helper function: (left child, right child)
# BAse case:
# if the left and right children don't exist, return True
# if either of them doesn't exist, return False
# compare if the value of the left and right children 
# if they are not same, return false
# return the recursive function func(self.left, self.right) and  func(self.right, self.left)


# Main function: (root)
# if the root doesn't exist, return True
# if the root exists, go over the left and right subtree nodes

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def is_symmetric_helper(left, right):
  #base case
  if not left and not right:
    return True

  if not left or not right:
    return False

  # recursive case
  if left.val != right.val:
    return False

  return is_symmetric_helper(left.left, right.right) and is_symmetric_helper(left.right, right.left)

def is_symmetric(root): # main func
  if not root:
    return True

  return is_symmetric_helper(root.left, root.right)

root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(is_symmetric(root))


root2 = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(2, None, TreeNode(3)))
print(is_symmetric(root2))

# Time complexity - O(n) because every node in the tree is checked
