#unit 8
#session 1
#ver 3
#prob 10

# can head be null or none?
# can the tree only contain only one node which is head? # False

# Happy Case:
#   5
#  / \
# 2   3
# True


# High Level plan
# initialize the var to keep track of the sum of the leaf node val
# go to the left subtree and right subtree until it reaches the leaf node
# if the curr node is the leaf node, add the val of the curr node to the sum var

# Low level plan
# start from the root
# a var to keep track of the root val and another var to keep track of the sum of the leaf node val
# go to left subtree and right subtree
# if the node is a leaf node
#   add the val to the sum vae
#  compare the root's val to the sum var

class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right

def sum_leaves(root):
  if not root:
    return False

  if not root.left and not root.right: #if the node is the leaf node
    return root.val 

  else:
    return sum_leaves(root.left) + sum_leaves(root.right)


def helper_func_leaf_sum(root):
  sum = sum_leaves(root)
  return(sum == root.val)
  
root = TreeNode(10, TreeNode(5), TreeNode(5))
print(helper_func_leaf_sum(root))

root1 = TreeNode(10)
print(helper_func_leaf_sum(root1))