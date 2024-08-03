#Unit 9
#session 2
#ver 1
#prob 1

from collections import deque

class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def level_order(root):
  # If the tree is empty:
  # return an empty list
  if root is None: 
    return []

  # Create an empty queue using deque
  queue = deque()

  # Create an empty list to store the explored nodes
  ex_nodes = []

  # Add the root to the queue
  queue.append(root)
  # While the queue is not empty:
  while queue:
    # Pop the next node off the queue (pop from the left side!)
    popped_node = queue.popleft()
    # Add the popped node to the list of explored nodes
    # print(popped_node.val, queue)
    ex_nodes.append(popped_node.val)

    # Add each of the popped node's childr en to the end of the queue
    if popped_node.left is not None:
      queue.append(popped_node.left)
    if popped_node.left is not None:
      queue.append(popped_node.right)


  return ex_nodes
