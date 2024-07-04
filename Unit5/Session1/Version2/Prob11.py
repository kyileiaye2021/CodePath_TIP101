#unit 5
#session 1
#ver 2
#prob 11

#["aries", "taurus", "gemini", "cancer"]
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

node_4 = Node('cancer')
node_3 = Node('gemini', node_4)
node_2 = Node('taurus', node_3)
node_1 = Node('aries', node_2)

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)