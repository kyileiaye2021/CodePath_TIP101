#unit 8
#session 2
#ver 1
#prob 5

# Example Input Tree #1: (tree depicted using keys)

#           10
#          /  \
#         /    \
#        5      15
#       / \    
#      1   8
#         / \
#        6   9

# Input: root = 10, current = 5
# Expected Output: 6 (Should return a node object)

# Time - O(n)
# Space - O(1)
class TreeNode():
  def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def inorder_successor(root, current):
  if not root:
    return None

  greatest_val = None # to keep track of the greatest val 
  succesor_node = None
  while root:

    if root.val > current:
      greatest_val = root.val
      root = root.left

    elif root.val == current:
      root = root.right

    else:
      root = root.right

  succesor_node = TreeNode(greatest_val)
  return succesor_node


root = TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(8, TreeNode(6), TreeNode(9))), TreeNode(15))
node = inorder_successor(root, 5) #6
print(node.val)

node1 = inorder_successor(root, 6) #8
print(node1.val)