#unit 9
#session 2
#ver 2
#prob 3

'''
Can the tree be empty? (-inf)
CAn the tree have only one node? (1)
Is it possible that all number of nodes in all levels are the same? ''' 

'''Happy Case'''
# Example Input Tree #1:

#       4
#      / \
#     2   6
#    / \  
#   1   3

# Example Input: root = 4
# Expected Output: 2
# Explanation: Levels 2 & 3 have 2 nodes each. 

# Example Input Tree #2:

#        1
#       / \
#      /   \
#     2     3
#    / \   / \ 
#   4   5 6   7

# Example Input: root = 1
# Expected Output: 4
# Explanation: Level 3 has 4 nodes, the most of any level

'''Edge case'''
# input - None, output - -inf
# input - TreeNode(1), output - 1

# BFS 
# create a queue
# put the root node to the queue
# initialize a var to keep track of the max num node 
# iterate until queue is empty
#   get the size of the queue
#   update the max num node 
#   pop the node from the left of the queue
#   put the children of popped node into the queue

from collections import deque

class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def level_max(root):
  max_num_node = float('-inf')
  
  if not root:
    return max_num_node
    
  queue = deque()
  queue.append(root)
  
  while queue:
    node_num = len(queue) # the num of nodes in each level
    
    max_num_node = max(max_num_node, node_num)

    for _ in range(node_num):
      popped_node = queue.popleft()
      
      if popped_node.left:
        queue.append(popped_node.left)

      if popped_node.right:
        queue.append(popped_node.right)

  return max_num_node

root = None
print(level_max(root)) # -inf

root2 = TreeNode(3)
print(level_max(root2)) # 1

root3 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(level_max(root3)) # 2

root4 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(level_max(root4)) # 4