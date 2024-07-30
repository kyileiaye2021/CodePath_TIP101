#unit 8
#session2
#ver 3
#prob 2

# Finding the least min val of the node in the tree
# We will go to the left subtree and find the leaf node
# if the root is none, return none

class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right

def tree_min(root):
  if not root:
    return None

  if not root.left:
    return root.val

  return tree_min(root.left)

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(tree_min(root))
root1 = None
print(tree_min(root1))