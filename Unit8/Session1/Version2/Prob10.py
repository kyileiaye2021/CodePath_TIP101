#unit 8
#session 1
#ver 2
#prob 10

# What if there is one node? # True
# What if the node is null? # True

# High Level Plan
# if the head node is null, return false
# Start from the head and check the curr node has 0 child or two children
# return true if it's the case
# otherwise false

'''
Time complexity - O(n)
Space complexity - O(n)'''
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def is_full_tree(root):
  #base case:
  if not root:
    return True

  #recursive case:
  if not root.left and not root.right: # have 0 children
    return True

  if root.left and root.right: # have two children
    return is_full_tree(root.left) and is_full_tree(root.right)

  return False

root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, TreeNode(5), TreeNode(20)))
print(is_full_tree(root))

root1 = TreeNode(10, TreeNode(5), None)
print(is_full_tree(root1))