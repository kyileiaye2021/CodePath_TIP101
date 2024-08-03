#unit 9
#session 1
#ver 2
#prob 4

'''
It is important that we need to make a list for second_min instead of var because
after a func is terminated, the var value get back to the original value
'''
# main func
# initialize first min to root's val and second min to inf
# call helper func
# if second min is still inf, return -1
# otherwise, return second min val

# helper func
# check if the curr val is greater than first min and less than second min
#   update the second min
# call recursive helper func on left and right subtree

'''
Time complexity - O(n) (every node in the tree is visited)
Space complexity - O(n)
'''
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def find_second_min_helper(root, first_min, second_min):
  if root:
    if first_min < root.val < second_min[0]:
      second_min[0] = root.val

    find_second_min_helper(root.left, first_min, second_min)
    find_second_min_helper(root.right, first_min, second_min)

def find_second_minimum_value(root):
  if not root or not root.left or not root.right:
    return -1

  first_min = root.val
  second_min = [float('inf')]

  find_second_min_helper(root, first_min, second_min)

  if second_min[0] < float('inf'):
    return second_min[0]
  else:
    return -1

root = TreeNode(2, TreeNode(2), TreeNode(5, TreeNode(5), TreeNode(7)))
print(find_second_minimum_value(root)) #5

root2 = TreeNode(1)
print(find_second_minimum_value(root2)) #-1

root3 = TreeNode(2, TreeNode(2), TreeNode(2))
print(find_second_minimum_value(root3)) #-1