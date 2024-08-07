#unit 9
#session 2
#ver 3
#prob 5

'''Edge CAse'''
# input - none. output - None
# input - TreeNode(3), output - 3 if it is either p or q

'''Happy Case'''
# Example Input Tree

#         3
#        / \
#       /   \
#      /     \
#     5       1
#    / \     / \  
#   6   2   0   8
#      / \  
#     7   4

# Example input: root = 3, p = 5, q = 1
# Expected Output: 3
# The LCA of nodes 5 and 1 is 3. 

# Example Input Tree

#         3
#        / \
#       /   \
#      /     \
#     5       1
#    / \     / \  
#   6   2   0   8
#      / \  
#     7   4

# Example input: root = 3, p = 5, q = 4
# Expected Output: 5
# The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself.

# DFS
# if the curr root is none, return none
# if the curr node val is either p or q, return current node
# recursively call on curr left subtree
# recursively call on curr right subtree
# if both are non-null, return curr node
# if left is non-null, return left and right is non-null, return right


class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def find_lca(root, p, q):
  # if the curr root is none, return none
  if not root:
    return None

  # if the curr node val is either p or q, return current node
  if root.val == p or root.val == q:
    return root.val

  # recursively call on curr left subtree
  # recursively call on curr right subtree
  left = find_lca(root.left, p, q)
  right = find_lca(root.right, p, q)

  # if both are non-null, return curr node
  if left and right:
    return root.val

  # if left is non-null, return left and right is non-null, return right
  return left if left else right

root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
print(find_lca(root, 5, 1)) #3
print(find_lca(root, 5, 4))

# Time complexity - O(n)
# Space complexity - O(n)