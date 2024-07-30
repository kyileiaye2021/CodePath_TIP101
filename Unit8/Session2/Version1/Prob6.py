#Unit 8
#session 2
#ver 1
#prob 6


# Example Input Trees: 

#           1                 2 
#          / \               / \
#         /   \             /   \
#        3     2           1     3
#       /                   \     \
#      5                     4     7

# Input: root1 = 1, root2 = 2
# Expected Output: 3
# Expected Output Tree

#       3
#      / \
#     /   \
#    4     5
#   / \     \  
#  5   4     7

#Time complexity - O(m+n)
#Space complexity - O(m+n)
class TreeNode():
  def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def merge_trees(root1, root2):
  #return none if root1 and root2 is none
  if not root1 and not root2:
    return None

  # if there is only one node in either of tree in that position, return that node
  if not root1:
    return root2

  if not root2:
    return root1

  #if there are nodes in both trees in the position, sum up the values of the nodes
  merged_root = TreeNode(root1.val + root2.val) # merged node for the nodes in each level
  merged_root.left = merge_trees(root1.left, root2.left)
  merged_root.right = merge_trees(root1.right, root2.right)

  return merged_root


  
  
  
  