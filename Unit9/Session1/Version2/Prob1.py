#unit 8
#session 1
#ver 2 
#prob 1

# if the curr node is not a leaf node, the value should be OR or AND
# if the curr node is a leaf node, the value should be True or False

# Base case:
 # if the curr node is a leaf node, just return the val

# REcursive case:
# if the curr node has children
# check if the curr val has OR or AND 
#   then, return the 

class TreeNode:

  def __init__(self, val=None, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def evaluate_tree(root):
  # Base Case
  # This will return leaf node value if the curr node is a leaf node

  if not root:
    return None

  if not root.left and not root.right:
    return root.val # True or False

  # REcursive case
  if root.val == 'OR':
    return evaluate_tree(root.left) or evaluate_tree(root.right)
  elif root.val == 'AND':
    return evaluate_tree(root.left) and eval(root.right)

root = TreeNode("OR", TreeNode(True), TreeNode("AND", TreeNode(False), TreeNode(True)))
print(evaluate_tree(root)) # True

root2 = TreeNode("OR", TreeNode('AND', TreeNode(False), TreeNode(False)), TreeNode("OR", TreeNode(False), TreeNode(False)))
print(evaluate_tree(root2)) #False

'''
Time Complexity: '''
