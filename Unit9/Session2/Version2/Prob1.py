#Unit 9
#session 2
#ver 2
#prob 1

from collections import deque # This is a popular library used for queues

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_by_level(root):
  # If the tree is empty:
    #return
  if not root:
    return

  # Create an empty queue using deque
  queue = deque()

  # Add the root to the queue
  visited = []

  queue.append(root)
  
  # While the queue is not empty:
  while queue:

    # Pop the next node off the queue (pop from the left side!)
    popped_node = queue.popleft()
    print(popped_node.val)

    # Print the popped node
    visited.append(popped_node.val)

    # Add each of the popped node's children to the end of the queue if they are not none
    if popped_node.left:
      queue.append(popped_node.left)

    if popped_node.right:
      queue.append(popped_node.right)

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print_by_level(root)
  
    
