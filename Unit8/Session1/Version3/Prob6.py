#Unit 8
#session 1
#ver 3
#prob 6

#pre-order traversal (current - left - right)

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def preorder_helper(root, lst):
  if not root:
    return lst

  lst.append(root.val) #current
  preorder_helper(root.left, lst) #left
  preorder_helper(root.right, lst) #right
  return lst

def preorder_traversal(root):
  lst = []
  return preorder_helper(root, lst)

root = TreeNode(1, TreeNode(2), TreeNode(3))
print(preorder_traversal(root)) # [1,2,3]

