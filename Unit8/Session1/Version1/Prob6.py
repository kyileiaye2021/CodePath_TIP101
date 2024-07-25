#unit 8
#session 1
#ver 1
#prob 6

# In-order traversal (left - current - right)
# time - O(n)
# space - O(n)
class TreeNode():
   def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

def inorder_helper(root, lst):
  #base case
  if not root:
    return lst

  inorder_helper(root.left, lst) #left
  lst.append(root.val) #current
  inorder_helper(root.right, lst) #right
  return lst
  
def inorder_traversal(root):
  lst = []
  return inorder_helper(root, lst)

root = TreeNode(1, TreeNode(2), TreeNode(3))
print(inorder_traversal(root)) # [2,1,3]