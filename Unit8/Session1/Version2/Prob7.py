#Unit 8
#session 1
#ver 2
#prob 7

#Binary Tree Product
# return the product of the node values
class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right

def product_tree(root):
  if not root:
    return 1
  return root.val * product_tree(root.left) * product_tree(root.right)

root = TreeNode(1, TreeNode(4), TreeNode(3))
print(product_tree(root))

