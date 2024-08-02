#unit 9
#session 1
#ver 2
#prob 3

# can the k value be greater than the total size of the tree?
# can the tree be none or have only one node?

# Main func
# initialized the empty list
# call the helper func
# iterate over the list until the kth smallest num


# Helper func (inorder traversal)
# if root is not None
# go to the left subtree 
# append the val to the list
# go to the right subtree

class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def inorder_traversal(root, lst):
  if root is not None:
    inorder_traversal(root.left, lst)
    lst.append(root.val)
    inorder_traversal(root.right, lst)

def kth_smallest(root,k):
  if not root:
    return 

  lst = []
  inorder_traversal(root, lst)

  return lst[k - 1]

root = TreeNode(15, TreeNode(10, TreeNode(8), TreeNode(12)), TreeNode(20, TreeNode(16), TreeNode(26)))
print(kth_smallest(root, 4)) #15

root2 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(kth_smallest(root2, 3)) #3