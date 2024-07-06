#unit 5
#session 2
#ver 1
#prob 3

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def add_first(head, new_node):
  new_node.next = head
  return new_node
  

node_1 = Node("Jigglypuff")
node_1.next = Node("Wigglytuff")

# Using the Linked List from Problem 2
print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)
