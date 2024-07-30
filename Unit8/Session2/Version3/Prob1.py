#Unit 8
#session 2
#ver 3
#prob 1

# Time complexity - O(n)
# Space complexity - O(n)
class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right

def count_odds(root):
  #base case:
  if not root:
    return 0

  #recursive case
  if root.val % 2 != 0:
    return 1 + count_odds(root.left) + count_odds(root.right)

  else:
    return count_odds(root.left) + count_odds(root.right)

root = TreeNode(2, TreeNode(4), TreeNode(6))
print(count_odds(root))
