#unit 9
#session 2
#ver 3
#prob 1

'''
Time complexity - O(n)
Space complexity - O(n)
'''
from collections import deque

class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def level_dict(root):
  # If the tree is empty:
  # return an empty dictionary
  if not root:
    return {}

  # Create an empty dictionary
  dict = {}
  # Create an empty queue using deque
  queue = deque()

  # Append a tuple (root, 1) to the queue. The queue will store tuples of (node, level)
  queue.append((root, 1))

  # While the queue is not empty:
  while queue:

    # Pop the next node, level pair off the queue (pop from the left side!)
    popped_node, depth = queue.popleft()

    # If the level is not yet a key in the dictionary
    if depth not in dict:
    # Add to dictionary with empty list as a value
      dict[depth] = [popped_node.val]

    else:
      dict[depth].append(popped_node.val) # append the val to the list of the corresponding depth key

  # Add a tuple with each of the popped node's children
  # and incremented level to the end of the queue
    if popped_node.left: # the popped node has left child
      queue.append((popped_node.left, depth + 1))
    if popped_node.right: # the popped node has right child
      queue.append((popped_node.right, depth + 1))

  return dict

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(level_dict(root))

root2 = TreeNode(4)
print(level_dict(root2))

root3 = None
print(level_dict(root3)) # none