#Unit 9
#session 2
#ver 2
# prob 5

'''Happy Case'''
# Example Input Tree:

#      1
#     / \
#    2   3
#   / \  
#  4   5

# Example Input: root = 1
# Output: 3 
# 3 is the length of the path [4,2,1,3] or [5,2,1,3]

'''Edge Case'''
# input - null, output - 0
# input - Treenode(3), output - 0

# helper func 
# check if the curr node is none
#   return 0
# recursively call on left subtree
# recursively call on right subtree
# update diameter with diameter and (right  + left)
# return 1 + left subtree + right subtree

# main func
# check if the root is none or has no child
#  return 0
# initialize diameter to 0
# call helper func
# decrement the returned val by 1
# return that val

class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def dfs(root, diameter):
  if not root:
    return 0

  left = dfs(root.left, diameter)
  right = dfs(root.right, diameter)

  diameter[0] = max(diameter[0], (left + right))
  return 1 + max(left, right)

def find_diameter(root):
  if not root or (not root.left and not root.right):
    return 0
  diameter = [0]
  dfs(root, diameter)
  return diameter[0]

root = None
print(find_diameter(root)) # 0

root3 = TreeNode(3)
print(find_diameter(root3)) #0

root2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(find_diameter(root2)) # 3


#time complexity - O(n)
#space complexity - O(n)