#unit 9
#session 1
#ver 1
#prob 4

# Binary search | in order traversal
# Main func
# initialize a list
# call the helper func 
# the list will be filled up with the node values in order
# create a root Treenode 
# iterate over the node from second ele
#    create a Treenode and connect

# Helper func
# if the curr node is not none
#   recursively call on the helper func on left subtree
#   append the value to the list
#   recursively call on the helper func on right subtree

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def inorder_traversal(root, lst):
  if root is not None:
    inorder_traversal(root.left, lst)
    lst.append(root.val)
    inorder_traversal(root.right, lst)
    
def increasing_bst(root):
  lst = []
  inorder_traversal(root, lst)
  
  modified_root = TreeNode(lst[0])
  current = modified_root
  
  for i in range(1, len(lst)):
    current.right = TreeNode(lst[i])
    current = current.right

root = TreeNode(5, TreeNode(1), TreeNode(7))
modified = increasing_bst(root)
print(modified.val)
print(modified.right.val)
print(modified.right.right.val)