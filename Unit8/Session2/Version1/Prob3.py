#unit 8
#session 2
#ver 1
#prob 3

class TreeNode():
   def __init__(self, key, value = 0, left=None, right=None):
       self.key = key
       self.val = value
       self.left = left
       self.right = right

def insert(root, key, value):
  if not root:
    return TreeNode(key, value) #insert the new node as root node if the tree is empty

  if key > root.key:
    root.right = insert(root.right, key, value) #don't forget to connect with the prev left or right 
  elif key < root.key:
    root.left = insert(root.left, key, value)
  else:  
    root.val = value # when the key is equal to the curr node's key
  return root
root = TreeNode( 10)
left = TreeNode(8)
right = TreeNode(15)
root.left = left
root.right = right
new_node = insert(root, 5, 0)
print(new_node.left.left.key)