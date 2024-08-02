#unit 9
#session 1
#ver 1
#prob 3


# Main func 
# param - root
# initialize empty list 
# call the helper func with empty list
# declare mindiff to the largest value in python
# iterate over the list 
# update the min diff with the difference between each element 
# return min diff

# Helper func
# param - root, min_diff
# Base case:
# if the curr node is not none
# recursively call on left subtree
# append the element in the lst
# recursively call on the right subtree

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def inorder_traversal(root, lst):
  if root is not None:
    inorder_traversal(root.left, lst)
    lst.append(root.val)
    inorder_traversal(root.right, lst)


def min_diff_in_bst(root):
  lst = []
  min_diff = float('inf')
  inorder_traversal(root, lst)
  for i in range(1, len(lst)):
    min_diff = min(min_diff, abs(lst[i] - lst[i - 1]))

  return min_diff

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(min_diff_in_bst(root))

root2 = TreeNode(1)
print(min_diff_in_bst(root2))