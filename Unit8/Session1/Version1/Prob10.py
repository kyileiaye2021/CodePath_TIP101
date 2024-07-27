#unit 8
#session 1
#ver 1
#prob 10

'''
return a list of values of leave nodes in descending order
'''

# Happy case:
# TreeNode(1, TreeNode(2), TreeNode(3)) -> [3,2]

# Edge case:
# Tree : None -> []

# High Level Plan
# use recursive method and binary search 
# base case: check the root is none or not
# recursive case: 
# call the func on the right subtree to get descending order
# append the ele
# call func on the left subtree

# Low Level Plan
# create a list
# check to see if the node is none
#  return []
# call right subtree
# append the element to the list
# call on left subtree
# return lst

class TreeNode():
   def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

def descending_leaves_recursive(root, lst):
  if not root:
    return lst
  descending_leaves_recursive(root.right, lst)
  
  if not root.left and not root.right:
    lst.append(root.val)
    
  descending_leaves_recursive(root.left, lst)
  return lst
def descending_leaves(root):
  lst = []
  return descending_leaves_recursive(root, lst)


lst = TreeNode(1, TreeNode(2), TreeNode(3))
print(descending_leaves(lst)) # [3,2]

lst2 = None
print(descending_leaves(lst2)) # []