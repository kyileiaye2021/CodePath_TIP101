#unit 9
#session 2
#ver 3
#prob 3

'''
Happy CAse
      1
     / \
    2   3
   / 
  4  
Input: root = 1, x = 4, y = 3
Expected Output: False

  1
 / \
2   3
 \   \
  4   5
Input: root = 1, x = 5, y = 4
Expected Output: True

    1
   / \
  2   3
   \   \
    4   5
Input: root = 1, x = 2, y = 3
Expected Output: False
'''

# BFS
# check if the tree is empty or thre is only one node, return False
# create a queue
# create a list for visited nodes
# create x_parent and y_parent
# put the root to the queue
# itearte until queue is empty
#   pop the node from left of the queue
#   check if the popped node'val is equal to x 
#      get the parent of the popped node and assign it to x_parent
#   if the popped node'val is equal to y
#      get the parent of the popped node and assign it to y_parent
#   put the popped node'val to the visited list
#   put the children of the node to the queue
# check if the x_parent and y_parent are not the same
#   return true
# return False

from collections import deque

class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def is_cousins(root, x, y):
  if not root or (not root.left and not root.right):
    return False

  queue = deque()
  visited = []
  x_parent = root.val
  y_parent = root.val
  x_depth = 0
  y_depth = 0

  queue.append((root, None, 1))

  while queue:

    level_size = len(queue)


    popped_node, parent, depth = queue.popleft()

    # check if the popped node is equal to x or y
    if popped_node.val == x:
      x_parent = parent
      x_depth = depth

    if popped_node.val == y:
      y_parent = parent
      y_depth = depth

    # add the popped node's val to the visited list
    visited.append(popped_node.val)

    # put the children of the popped node to the queue
    if popped_node.left:
      queue.append((popped_node.left, popped_node.val, depth + 1))

    if popped_node.right:
      queue.append((popped_node.right, popped_node.val, depth + 1))

  return (x_depth == y_depth) and (x_parent != y_parent)

root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(is_cousins(root, 4, 3)) #False

root1 = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
print(is_cousins(root1, 5, 4)) # True
print(is_cousins(root1, 2, 3)) # False 
