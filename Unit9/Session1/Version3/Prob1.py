#unit 9
#session 1
#ver 3
#prob 1

# Build a Binary Tree III

# Example Input Tree

#         +
#       /   \
#      /     \
#     *       -
#    / \     / \
#   5   2   60 20 

# Input: root = +
# Expected Output: 50
# Explanation:

#         +                         +
#       /   \                     /  \
#      /     \         -->       10  40          -->    50
#     *       -               
#    / \     / \
#   5   2   60 20 

# if there is only one node in the tree, return that node.val
# if there is no nodes in the tree, return 0

# if the curr node is a leaf node, return the val of curr node
# if the curr node has two children
#   check the curr node's operator val
#    call recursive funcs on left and right subtree with that operator


class TreeNode:
  def __init__(self, val=None, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def evaluate_tree(root):
  if not root: # if there is no node
    return 0

  if not root.left and not root.right: # if there is only one node in the tree or the curr node is a leaf
    return root.val

  # if the node has two children
  if root.val == "+":
    return evaluate_tree(root.left) + evaluate_tree(root.right)
  elif root.val == "-":
    return evaluate_tree(root.left) - evaluate_tree(root.right)
  elif root.val == "*":
    return evaluate_tree(root.left) * evaluate_tree(root.right)
  else:
    return evaluate_tree(root.left) / evaluate_tree(root.right)

root = TreeNode("+", TreeNode("*", TreeNode(5), TreeNode(2)), TreeNode("-", TreeNode(60), TreeNode(20)))
print(evaluate_tree(root)) #50

root1 = TreeNode(4)
print(evaluate_tree(root1)) # 4

root2 = None
print(evaluate_tree(root2)) #None


