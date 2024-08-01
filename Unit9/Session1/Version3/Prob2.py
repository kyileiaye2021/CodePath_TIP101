#unit 9
#session 1
#ver 3
#prob 2

# Cloned tree

# base case:
# if the curr node is none, return none
# if the curr node of orig tree is the same as the target node, return the corresponding clone node
# go to the left subtree of the orig tree
#  If the target is found in the left subtree, return the result.
# go to the right subtree of the orig tree and return the result

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right


def get_target_copy(original, cloned, target):
  if not original:
    return None

  if original.val == target:
    return cloned

  left_result = get_target_copy(original.left, cloned.left, target)
  right_result = get_target_copy(original.right, cloned.right, target)

  if left_result:
    return left_result
  else:
    return right_result


root = TreeNode(7, TreeNode(4), TreeNode(3, TreeNode(6), TreeNode(19)))
ref_copy = get_target_copy(root, root, 3)
print(ref_copy.val)
