#unit 8
#session 2
#ver 2
#prob 5

class TreeNode():
  def __init__(self, value, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def inorder_predecessor(root, current):
  predecessor = None
  while root:
      if current.val < root.val:
          root = root.left
      elif current.val > root.val:
          predecessor = root
          root = root.right
      else:
          if root.left:
              predecessor = find_max(root.left)
          break
  return predecessor

def find_max(node):
  current = node
  while current.right:
      current = current.right
  return current

# Constructing the tree for test cases
root1 = TreeNode(10, TreeNode(5, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(8)), TreeNode(15))
root2 = TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(8, TreeNode(6), TreeNode(9))), TreeNode(15))

# Test case 1
node1 = inorder_predecessor(root1, root1.left)  # current = 5 in the first tree
print(node1.val)  # Expected output: 3

# Test case 2
node2 = inorder_predecessor(root2, root2.left.right.right)  # current = 9 in the second tree
print(node2.val)  # Expected output: 8
