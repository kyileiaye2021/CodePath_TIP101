#Unit 8
#session 1
#ver 3
#prob 2

class TreeNode:
  def __init__(self, value, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right


def tree_expression(root):
  if root.val == "OR":
    return root.left.val or root.right.val

  else:
    return root.left.val and root.right.val
  
root = TreeNode('OR')
left_child = TreeNode(True)
right_child = TreeNode(False)
root.left = left_child
root.right = right_child

root2 = TreeNode('AND')
left_child2 = TreeNode(True)
right_child2 = TreeNode(False)
root2.left = left_child2
root2.right = right_child2

print(tree_expression(root))
print(tree_expression(root2))