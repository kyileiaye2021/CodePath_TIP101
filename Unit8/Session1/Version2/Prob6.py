#Unit 8
#session 1
#ver 2
#prob 6

# post-order traversal (left, right, current)
# Time - O(n)
# Space - O(n)
class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right

def postorder_helper(root, lst):
  # base case
  if not root:
    return lst

  postorder_helper(root.left, lst) #left
  postorder_helper(root.right, lst) #right
  lst.append(root.val) #current
  return lst

def postorder_traversal(root):
  lst = []
  return postorder_helper(root, lst) 


root = TreeNode(1, TreeNode(2), TreeNode(3))
print(postorder_traversal(root)) # [2,3,1]
