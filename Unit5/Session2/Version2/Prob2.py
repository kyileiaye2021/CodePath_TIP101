#unit 5
#session 2
#ver 2
#prob 2

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

node_4 = Node('Ken')
node_3 = Node('Weird Barbie', node_4)
node_2 = Node('President Barbie', node_3)
node_1 = Node('Barbie', node_2)

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)

'''Example Output:

Barbie -> President Barbie
President Barbie -> Weird Barbie
Weird Barbie -> Ken
Ken -> None'''