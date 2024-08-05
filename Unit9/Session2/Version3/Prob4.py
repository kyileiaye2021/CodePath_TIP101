# unit 9
# session 2
# ver 3
# prob 4


'''Edge Case'''
# input - None, output - None
# input - TreeNode(6), output - 6

'''Happy CAse'''
# Example Input Tree 

#       6
#      / \
#     3   8
#    /   / \  
#   5   4   2
#      / \   \
#     1   7   3

# Expected Output: (Printed)
# 6
# 3
# 8
# 5 
# 2
# 1
# 3
# Explanation:
# Level 1: first and last node is 6
# Level 2: first node in 3, last node is 8
# Level 3: first node is 5, last node is 2
# Level 4: first node is 1, last node is 3

# BFS
# create a queue
# put the root node to the queue
# iterate over the queue unti the queue is empty
  # get the level size 
  # first node = peek the node from the left
  # last node = peek the node from the right
  # print first and last node in each level
  # iterate for the level size
    # pop the node from the queue
    # put the children of each popped node into the queue

from collections import deque

class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right


def print_corner_nodes(root):
  if not root:
    return None

  queue = deque()
  queue.append(root)

  while queue:
    level_size = len(queue)
    first_node = queue[0]
    last_node = queue[level_size - 1]

    print(first_node.val) 
    if first_node.val != last_node.val:
      print(last_node.val)

    for _ in range(level_size):
      popped_node = queue.popleft()

      if popped_node.left:
        queue.append(popped_node.left)

      if popped_node.right:
        queue.append(popped_node.right)


root = None
print_corner_nodes(root) #None

root1 = TreeNode(2)
print_corner_nodes(root1) #2

root2 = TreeNode(6, TreeNode(3, TreeNode(5)), TreeNode(8, TreeNode(4, TreeNode(1), TreeNode(7)), TreeNode(2, None, TreeNode(3))))
print_corner_nodes(root2) #6 3 8 5 2 1 3