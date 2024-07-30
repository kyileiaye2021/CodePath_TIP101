#unit 8
#session 2
#ver 1
#prob 4

#remove the node from BST tree (in-order successor)

class TreeNode():
   def __init__(self, key, value, left=None, right=None):
       self.key = key
       self.val = value
       self.left = left
       self.right = right

def find_min(node):
  current = node
  if not current.left:
    current = current.left
  return current.val
  
def remove_bst(root, key):
# Locate the node to be removed
  if key < root.val:
    root.left = remove_bst(root.left, key)
  elif key > root.val:
    root.right = remove_bst(root.right, key)
  else: #if the key is found
    
    #node with one child or no children
    if not root.left: # has only one right child
      return root.right
    elif not root.right: #has only one left child
      return root.left

    # node with two children
    temp_val = find_min(root.right)
    root.val = temp_val
    root.right = remove_bst(root.right, temp_val)

  return root
    
# If the node is a leaf node:
  # Remove the node by redirecting the appropriate child reference of its parent to None
# If the node has one parent:
  # Replace the node with its child, updating its parent's nodes child reference appropriately
# If the node has two children:
  # Find the node's inorder successor (smallest node in right subtree)
  # Swap the value of the node and its inorder successor
  # Recursively remove the successor (which now has the current node's value)
# Return the root of the updated tree