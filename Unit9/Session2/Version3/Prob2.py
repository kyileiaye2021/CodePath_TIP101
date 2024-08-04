#unit 9
#session 2
#ver 3
#prob 2

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

# Example input: root = 3, start_level = 2, end_level = 4
# Expected Output: [5, 1, 6, 2, 0, 8, 7, 4]
# Explanation:
# Level 2 nodes: 5, 1
# Level 3 nodes: 6, 2, 0, 8
# Level 4 nodes: 7, 4

# Edge case:
# input: root = None, return []

# if the root is none, return []
# initialize the queue and empty list
# put the root to the queue with the val of depth 1
# itereate until the queue is none
#   pop the ele from the queue
#   check the depth is greater than or equal to start level and less than or equal to end level
#   append it to the list
# append the children of popped_node to the queue

from collections import deque

class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def get_level_range(root, start_level, end_level):

  if not root:
    return []

  queue = deque()
  res_lst = []

  queue.append((root, 1))

  while queue:

    popped_node, depth = queue.popleft()

    if depth >= start_level and depth <= end_level:
      res_lst.append(popped_node.val)

    if popped_node.left:
      queue.append((popped_node.left, depth + 1))

    if popped_node.right:
      queue.append((popped_node.right, depth + 1))

  return res_lst

root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
print(get_level_range(root, 2, 4)) #[5, 1, 6, 2, 0, 8, 7, 4]

root1 = None
print(get_level_range(root1, 0, 0))

root2 = TreeNode(3, TreeNode(5, TreeNode(4)))
print(get_level_range(root2, 1, 3)) # [3,5,4]