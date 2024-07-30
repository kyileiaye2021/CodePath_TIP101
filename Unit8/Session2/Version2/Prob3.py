#unit 8
#session 2
#ver 2
#prob 3

class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right

def insert_with_duplicates(root, value):
  #base case
  # if the node is a leaf node, create a new node using value
  # and connect the leaf node to it
    if not root: #important: we need to create a new node if only we reach the last node
        new_node = TreeNode(value)
        return new_node

    if value >= root.val:
        root.right = insert_with_duplicates(root.right, value)

    else:
        root.left = insert_with_duplicates(root.left, value)
    return root

root = TreeNode(20, TreeNode(10), TreeNode(30))
value = 25
root = insert_with_duplicates(root, value)
print(root.right.val)
print(root.right.left.val)
