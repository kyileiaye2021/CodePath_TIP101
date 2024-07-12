#unit 6
#session 1
#ver 3
#prob 4

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def has_cycle(head):
  slow = head
  fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
      return True

  return False


head = Node(1)
node_2 = Node(2)
node_3 = Node(3)
head.next = node_2
node_2.next = node_3
node_3.next = head
print(has_cycle(head))

# Input List:
# 1 -> 2 -> 3 -> 1
#      ^         | 
#      |---------|
# Input: head = 1