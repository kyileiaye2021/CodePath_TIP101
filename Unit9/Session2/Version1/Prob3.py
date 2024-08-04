# Unit 9
# sessino 2
# ver 1
# prob 3

#Odd-Even Level Sum Difference in Binary Tree

'''
Can the tree be empty?
Can the tree has only one level? 
Can the nodes in the tree contain neg val?

Happy case:
* input - None, output - 0

* input - 3, output - 3 there is no even level

* input - 6  output - -5
         / \
        3   8
       /   / \  
      5   4   2
         / \   \
        1   7   3
'''

# BFS (operating the nodes level by level)
# initialize the queue to store each node in the tree
# put the tuple of root node with the depth val of 1 to the queue
# initialize the even_sum and odd_sum to 0 to keep track of the totol sum of even and odd levels
# whiile thre are elements in queue
  # create level size to keep track of the total num of nodes in that level
  # create a for loop to loop around the num in each level to get the sum of each level
    # pop the ele from the left side of queue
    # check if the depth of popped-node is even or odd
      # update the even_sum and odd_sum according to the corresponding depth
    # put the children of the popped_node into the queue if they exist

# diff = odd_sum - even_sum
# return diff

# Time complexity - O(n)
# Space complexity - O(n)
from collections import deque

class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def level_difference(root):
  if not root:
    return 0
  queue = deque()
  queue.append((root, 1))
  even_sum, odd_sum = 0, 0

  while queue:

    level_size = len(queue)

    for _ in range(level_size):
      popped_node, depth = queue.popleft()

      if depth % 2 == 0:
        even_sum += popped_node.val

      else:
        odd_sum += popped_node.val

      if popped_node.left:
        queue.append((popped_node.left, depth + 1))

      if popped_node.right:
        queue.append((popped_node.right, depth + 1))

  diff = odd_sum - even_sum
  return diff

root = None
print(level_difference(root)) # 0

root2 = TreeNode(2)
print(level_difference(root2)) # 2

root3 = TreeNode(6, TreeNode(3,TreeNode(5)), TreeNode(8, TreeNode(4, TreeNode(1), TreeNode(7)), TreeNode(2, None, TreeNode(3))))
print(level_difference(root3)) #-5
