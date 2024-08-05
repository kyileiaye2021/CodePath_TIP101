#unit 9
#session 2
#ver 1
#prob 4

'''
Edge cases:
input - None, out - [[]]
input - TreeNode(3), outs - [[3]]

Happy Cases:
Input Tree
   3
  / \
 9  20
    / \
   15  7

[[3], [9,20], [15,7]]
'''

#BFS
# create a queue
# create a total list to store the level list

# put the root to the queue 

# iterate until the queue is empty
  # level_size 
  # create a list to store the level lists

  # iterate for that level_size
    # pop the ele from the queue
    # put the node val in the level lst
    # put the children of the popped node into the queue

  # append each level lst to the total lst

#return level lst

# Time complexity - O(n)
# Space complexity - O(n)
from collections import deque
class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def level_order(root):
  if not root:
    return [[]]

  queue = deque()
  total_lst = []

  queue.append(root)

  while queue:

    level_lst = []
    level_size = len(queue)

    for _ in range(level_size):
      popped_node = queue.popleft()
      level_lst.append(popped_node.val)

      if popped_node.left:
        queue.append(popped_node.left)
      if popped_node.right:
        queue.append(popped_node.right)

    total_lst.append(level_lst)

  return total_lst

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(level_order(root)) #[[3], [9,20], [15,7]]

root1 = TreeNode(3)
print(level_order(root1)) #[[3]]

root2 = None
print(level_order(root2)) #[[]]
