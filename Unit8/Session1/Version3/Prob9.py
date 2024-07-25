#Unit 8
#session 1
#ver 3
#prob 9

# Any node greater than value in the tree
class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right

'''
Since we want greater node, need to go to the right side
but, it there is no right side, we have to go to the left side and check there are right subnode
greater than value
If the node becomes null, return false

Time - O(logn)
Space - O(logn)
'''
def contains_greater_bst(root, value):
  if not root:
    return False

  if root.val > value:
    return True

  if root.right:
    return contains_greater_bst(root.right, value)
  else:
    return contains_greater_bst(root.left, value)

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(contains_greater_bst(root, 6)) #False
print(contains_greater_bst(root, 0)) #True
