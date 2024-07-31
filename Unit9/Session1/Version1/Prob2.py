#Unit 9
#sesion 1
#ver 1
#prob 2

#PRoblem 2:Root-to-Leaf Paths

# Helper Func
# Base case
# the current root doesn't exist, return ''

# recursive case
# append the current node's val to the str
# if the current node is a leaf node, append the str to the list
# call on recursive func on left and right subtree

# if there are two children
# call the recursive func for both left and right subtrees 


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def binary_tree_paths_helper(root, res_lst, temp_str):
  # base case
  if not root: # return empty str
    return "" 

  if temp_str:
    temp_str += '->' + str(root.val) 
  else:
    temp_str += str(root.val)
    
  if not root.left and not root.right: #if the curr node is a leaf node
    res_lst.append(temp_str)

  else:
    binary_tree_paths_helper(root.left, res_lst, temp_str)
    binary_tree_paths_helper(root.right, res_lst, temp_str)

def binary_tree_paths(root):
  res_lst = []
  temp_str = ""
  binary_tree_paths_helper(root, res_lst, temp_str)
  return res_lst


root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
lst = binary_tree_paths(root)
print(lst)

root2 = TreeNode(1)
lst = binary_tree_paths(root2)
print(lst)