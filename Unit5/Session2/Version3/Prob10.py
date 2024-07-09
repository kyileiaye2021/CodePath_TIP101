#unit 5
#session 2
#ver 3
#prob 10

class Node:
  def __init__(self, value, next=None, prev=None):
      self.value = value
      self.next = next
      self.prev = prev

def get_length(node):
  length = 0
  curr_head = node
  while curr_head:
    length += 1
    curr_head = curr_head.next

  curr_head = node.prev
  while curr_head:
    length += 1
    curr_head = curr_head.prev

  return length

node_4 = Node(7)
node_3 = Node(6, node_4)
node_2 = Node(5, node_3)
node_1 = Node(3, node_2)
node_4.prev = node_3
node_3.prev = node_2
node_2.prev = node_1

print(get_length(node_3))

# List: 3 <-> 5 <-> 6 <-> 7
# Input: node = 6
# Output: 4
