#unit 8
#session 2
#ver 3
#prob 4

class TreeNode():
   def __init__(self, key, value, left=None, right=None):
       self.key = key
       self.val = value
       self.left = left
       self.right = right

def merge(left_root, right_root):
  current = left_root
  while current.right:
    current = current.right

  #connect the left and right subtree
  current.right = right_root
  
  return left_root
  
def remove_bst(root, key):
  if not root:
    return None
  if key < root.val:
    root.left = remove_bst(root.left, key)
  elif key > root.val:
    root.right = remove_bst(root.right, key)
  else:
    if not root.left:
      return root.right
    elif not root.right:
      return root.left
    else:
      return merge(root.left, root.right)
  return root

root = TreeNode(20, TreeNode(10, TreeNode(5), TreeNode(15)), TreeNode(30))
key = 20
root = remove_bst(root, key)
print(root.right.right.val)