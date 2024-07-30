#unit 8
#session 2
#ver 3
#prob 6

# Time complexity - O(n*m)
# Space complexity - O(n)
class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right

def is_identical(root, sub_root):
  if not root and not sub_root: #both nodes are none
    return True
    
  if not root or sub_root: #only one node is none
    return False

  if root.val != sub_root.val:
    return False

  return is_identical(root.left, sub_root.left) and is_identical(root.right, sub_root.right)
    
def is_subtree(root, sub_root):
  # if the sub_root is empty, return True (empty subtree is the subtree of every tree)
  if not sub_root:
    return True

  #if the root is empty, return False (non-empty subtree cannot be the subtree of empty tree)
  if not root:
    return False

  if is_identical(root, sub_root):
    return True

  return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root) # the subtree can be either side of the subtree

  
  

  
