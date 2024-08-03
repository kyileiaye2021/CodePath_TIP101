#unit 9
#session 1
#ver 3
#prob 5

# main func
# if the curr node is null, return 0
# keep track of the curr node val with a orig temp var
# calculate the sum and assign it to the curr val
# return the sum of curr orig val + left sum + right sum

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def sum_replace(root):
  if not root:
    return 0

  left_sum = sum_replace(root.left)
  right_sum = sum_replace(root.right)

  original_node = root.val
  root.val = left_sum + right_sum
  return original_node + root.val

def sum_transform(root):
  sum_replace(root)
  return root.val

root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7), TreeNode(8)), TreeNode(6)))
print(sum_transform(root))

# Time complexity - O(n)
# Space complexity - O(n)