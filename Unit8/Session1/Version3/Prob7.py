#Unit 8
#session 1
#ver 3
#prob 7

class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right

def is_lesser(root,value):

   if not root:
      return True

   if root.val < value:
      return is_lesser(root.left, value) and is_lesser(root.right, value)
   else: 
      return False

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(is_lesser(root, 6))
      

      
