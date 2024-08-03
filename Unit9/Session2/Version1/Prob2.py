#Unit 9
#session 2
#ver 1
#prob 2

# Happy Case:
#    3
#   / \
#  9  20
#     / \  
#    15  7
# input - 3, output - 2

# Edge Cases:
# * input - None, output - 0
# * input - 3, output - 1

# # BFS is the best for finding shortest path in BST
# check if the root is none
#  return 0

# initialize deque and list to store the children of each node and visited nodes
# put the root node to the deque with the depth value of 1
# pop the deque from the left 
# check if the popped_node is a leaf node
#  return the depth right away
# check if there is a left child
#  put the popped_node's left child to the deque and increment the depth val by 1
# check if there is a right child
#  put the popped_node's right child to the deque and increment the depth val by 1

from collections import deque

class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right


def min_depth(root):
  if not root:
    return 0

  queue = deque()
  visited = []

  queue.append((root, 1))

  while queue:
    # pop the node from the left
    popped_node, depth = queue.popleft()

    # check the popped node is a leaf (getting the shortest path)
    if not popped_node.left and not popped_node.right:
      return depth

    #put the popped node's val to the visited list
    visited.append(popped_node.val)

    # check if the popped node has left child
    if popped_node.left:
      queue.append((popped_node.left, depth + 1))

    # check if the popped node has right child
    if popped_node.right:
      queue.append((popped_node.right, depth + 1))

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(min_depth(root)) #2

root1 = TreeNode(3)
print(min_depth(root1)) #1

root2 = None
print(min_depth(root2)) #0  
