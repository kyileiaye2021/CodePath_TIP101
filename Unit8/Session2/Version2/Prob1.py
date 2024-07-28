#Unit 8
#session 2
#version 2
#prob 1

# Time complexity - O(n) we have to visit every node to check the val is even or odd
# Space complexitu - O(n) the recursive depth equals to the num of func being called
class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right

def is_even(root):
  if not root:
    return True

  if root.val % 2 == 0:
    return is_even(root.left) and is_even(root.right)

  else:
    return False

root = TreeNode(4, TreeNode(5), TreeNode(8))
print(is_even(root))
