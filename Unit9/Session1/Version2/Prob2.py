#unit 9
#session 1
#ver 2
#prob 2

# Lonely node

# Helper func
# if the curr node is none, 
#   return
# if the curr node has only right child
#   append the left child to the lst
# otherwise append the left child

# Main func
# if there is only one root node or no nodes in the tree, return the empty lsi
# call the helper func
# return the lst

'''Time complexity: O(n)'''
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def find_lonely_nodes_helper(root, res_lst):
  # BAse case
  if not root:
    return

  #recursive case 
  if not root.right and root.left: # if there is only left child
    res_lst.append(root.left.val)

  elif not root.left and root.right: # if there is only right child
    res_lst.append(root.right.val)

  # if there are both left and right
  find_lonely_nodes_helper(root.left, res_lst)
  find_lonely_nodes_helper(root.right, res_lst)

def find_lonely_nodes(root):
  res_lst = []
  if not root or (not root.left and not root.right):
    return res_lst
  find_lonely_nodes_helper(root, res_lst)
  return res_lst

root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(find_lonely_nodes(root)) # [4]

root1 = TreeNode(1)
print(find_lonely_nodes(root1)) # []

root2 = None
print(find_lonely_nodes(root2)) #[]