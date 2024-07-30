#unit 8
#session 2
#ver 2
#prob 4

# remove the node from BST tree (in-order predecessor) # right most node in left subtree

class TreeNode():
   def __init__(self, key, value, left=None, right=None):
       self.key = key
       self.val = value
       self.left = left
       self.right = right

def find_max(node):
  current = node
  while current.right:
    current = current.right
  return current.val
  
def remove_bst(root, key):
  # find the node to be deleted
  if not root:
    return None
    
  if key < root.val:
    root.left = remove_bst(root.left, key)
  elif key > root.val:
    root.right = remove_bst(root.right, key)
  else:
    #node with no or one child
    if not root.left:
      return root.right
    elif not root.right:
      return root.left

    # node with two children

    temp_val = find_max(root.left)
    root.val = temp_val
    root.left = remove_bst(root.left, temp_val)

  return root