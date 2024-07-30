#unit 8
#session 2
#ver 3
#Prob 3

# BST insertion
# Time complexity - O(n)
# Space complexity - O(n) 

class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right

def insert_with_duplicates(root, value):
  if not root:
    new_node = TreeNode(value)
    return new_node

  if root.val >= value:
    root.left = insert_with_duplicates(root.left, value)
  else:
    root.right = insert_with_duplicates(root.right, value)
  return root

root = TreeNode(20, TreeNode(10), TreeNode(30))
value = 25
root = insert_with_duplicates(root, value)
print(root.right.left.val) #25

root1 = TreeNode(20, TreeNode(10), TreeNode(30))
value = 20
root1 = insert_with_duplicates(root1, value)
print(root1.left.right.val) # 20

