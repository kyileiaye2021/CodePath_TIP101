#unit 9
#session 2
#ver 1
#prob 5

# DFS
# helper func (root, sum)
# if the curr node is none, return 0
# right = root.val + helper(root.right, sum) + helper(root.left, sum)
# left = root.val + helper(root.left, sum) + helper(root.right, sum)
# sum += right - left

# main func(root)
# return 0 if the root has 0 nodes
# initialize total_tilts to 0
# call helper func
# return total_tilts

class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def find_tilt_helper(root, total_tilt):
  if not root:
    return 0

  left = find_tilt_helper(root.left, total_tilt)
  right = find_tilt_helper(root.right, total_tilt)

  tilt = abs(right - left)
  total_tilt[0] += tilt

  return root.val + left + right

def find_tilt(root):
  if not root or (not root.left and not root.right):
    return 0

  total_tilt = [0]
  find_tilt_helper(root, total_tilt)
  return total_tilt[0]

root = TreeNode(1, TreeNode(2), TreeNode(3))
print(find_tilt(root))

root1 = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, None, TreeNode(7)))
print(find_tilt(root1))



