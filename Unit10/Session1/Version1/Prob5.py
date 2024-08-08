# unit 10
# session 1
# ver 1
# prob 5

'''Edge case'''
# input - None, output - 0
# iinput - TreeNode(2), output - 2

'''Happy case'''
#     4
#    / \
#   9   0
#  / \
# 5   1
# 495 + 491 + 40 = 1026

# Plan 
# DFS

# main func
# if the curr node is none, return 0
# if the curr node has no children, return the curr node val
# initialize total_sum to 0
# call the helper func
# return total_sum

# helper func ( root, total_sum, path_str )
# if the curr node is null, 
#   convert the path_str to int and add that int val to the total_sum
# convert the curr node val to str and concatenate it to path_str
# recursively call helper func on left subtree
# recursively call helper func on right subree

# Implement

class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def dfs(root, total_sum, path_str):
  if not root:
    return 

  path_str += str(root.val)

  if not root.left and not root.right:
    total_sum[0] += int(path_str)

  dfs(root.left, total_sum, path_str)
  dfs(root.right, total_sum, path_str)


def sum_numbers(root):
  if not root:
    return 0

  if not root.left and not root.right:
    return root.val

  total_sum = [0]
  path_str = ""
  dfs(root, total_sum, path_str)
  return total_sum[0]

root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
print(sum_numbers(root)) #1026

root = None
print(sum_numbers(root)) # 0

root = TreeNode(2)
print(sum_numbers(root)) #2
