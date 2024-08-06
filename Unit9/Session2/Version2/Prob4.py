#unit 9
#session 2
#ver 2
#prob 4

# Happy cases:
# Input: root = [3,9,20,null,null,15,7]
#Output: [[9],[3,15],[20],[7]]

# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]

# Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
# Output: [[4],[9,5],[3,0,1],[8,2],[7]]

# Edge cases:
# input: [null]
# output: [[]]

# BFS with hashmap/ queue/ list
# return empty lst if the tree is none
# create a queue to store each node with its column index in the tree
# create a hashmap to store the column index as key and a list of node val as values
# create a list to store the value of hashmap
# put the root of the tree into queue
# iterate until queue is empty
#    pop out the node and put it in the hashmap according to corresponding column index
#    if there is a left child of popped node, put it in the queue
#    if there is a right child of popped node, put it in the queue
# sort the dict by column index and put the value lsts in the lst
# return the lst

from collections import deque
from typing import Text

class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def vertical_order(root):
  if not root:
    return []

  queue = deque()
  column_dict = {}
  res_lst = []

  queue.append((root, 0))

  while queue:
    node, column_index = queue.popleft()

    if column_index not in column_dict:
      column_dict[column_index] = [node.val]

    else:
      column_dict[column_index].append(node.val)

    if node.left:
      queue.append((node.left, column_index -1))

    if node.right:
      queue.append((node.right, column_index + 1))

  for key in sorted(column_dict):
    res_lst.append(column_dict[key])

  return res_lst

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(vertical_order(root)) # [[9],[3,15],[20],[7]]

root1 = TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7)))
print(vertical_order(root1)) # [[4],[9],[3,0,1],[8],[7]]

root2 = TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0, TreeNode(5))), TreeNode(8, TreeNode(1, None, TreeNode(2)), TreeNode(7)))
print(vertical_order(root2)) # [[4],[9,5],[3,0,1],[8,2],[7]]

root3 = None
print(vertical_order(root3)) # []
# time complexity - O(nlogn) also sort the dict
# space complexity - O(n)