#unit 9
#session 2
#ver 2
#prob 2

# if the root is none, return 
# create a dict
# create a sum list
# create a queue
# create a visited list

# put the root node in the queue with the value of depth 1
# while the queue is not none
  # pop the node from the left 
  # if the depth key is not in the dictionary, put the key value in the dict
  # if the depth key is already in the dictionary, update the value in the dict
  # add the node's val to the visited list
  # add the children of the visited node to the queue with updated depth
# add the dict value to the sum list

from collections import deque

class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right


def level_sum(root):
  if not root:
    return []
  dict = {}
  sum_lst = []
  queue = deque()
  visited = []

  queue.append((root, 1))

  while queue:
    popped_node, depth = queue.popleft()

    if depth not in dict:
      dict[depth] = popped_node.val

    else:
      dict[depth] += popped_node.val

    visited.append(popped_node.val)

    if popped_node.left:
      queue.append((popped_node.left, depth + 1))
    if popped_node.right:
      queue.append((popped_node.right, depth + 1))

  for level_sum in dict.values():
    sum_lst.append(level_sum)

  return sum_lst

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(level_sum(root))
    

'''
# 1) If the tree is empty, return an empty list.
# 2) Create an empty queue and add the root node.
# 3) Create an empty list to store the result.
# 4) While the queue is not empty:
#     a) Get the number of nodes at the current level.
#     b) Initialize the sum for the current level to 0.
#     c) For each node at the current level:
#         i) Pop the node from the queue.
#         ii) Add its value to the current level sum.
#         iii) Add the left child to the queue if it exists.
#         iv) Add the right child to the queue if it exists.
#     d) Add the current level sum to the result list.
# 5) Return the result list.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_sum(root):
    if not root:
        return []

    queue = deque()
    sum_lst = []

    queue.append(root)

    while queue: # each iteration represents each level
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            popped_node = queue.popleft()
            level_sum += popped_node.val

            if popped_node.left:
                queue.append(popped_node.left)
            if popped_node.right:
                queue.append(popped_node.right)

        sum_lst.append(level_sum)

    return sum_lst

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(level_sum(root))


'''
