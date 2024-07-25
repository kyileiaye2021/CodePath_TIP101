#unit 8
#session 1
#ver 1
#prob 7

# size of tree (total numbers of nodes)
'''
Using pre-order traversal method to count the node'''
class TreeNode():
   def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

def size(root):

  if not root:
    return 0

  return 1 + size(root.left) + size(root.right)

root = TreeNode(1, TreeNode(2), TreeNode(3))
print(size(root))
