#unit 6
#session 1
#ver 2
#prob 2

#find max value in ll

# low level planning
# * create a temp pointer to represent the head and tranverse the ll
# * create a max var to keep track of the max val first initialized to smallest val
# * tranverse starting from the head of the ll until the node is none
#   * check the val if it is greater than the max var
#     * update the max value
# * return the max val
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def find_max(head):
  curr_head = head
  max_val = float('-inf')
  while curr_head:
    if curr_head.value > max_val:
      max_val = curr_head.value
    curr_head = curr_head.next
  return max_val

head = Node(5, Node(6, Node(7, Node(8))))
max_value = find_max(head)
print(max_value)
# Linked List: 5 -> 6 -> 7 -> 8 
# Input: head = 5
# Expected Output: 8
