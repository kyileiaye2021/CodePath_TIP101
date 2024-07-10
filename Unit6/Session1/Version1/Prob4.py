#unit 6
#session 1
#ver 1
#prob 4

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle_element(head):
  fast, slow = head, head
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
  return slow.value

even_ll = Node(1, Node(2, Node(3, Node(4)))) #1,2,3,4
odd_ll = Node(1, Node(2, Node(3))) #1,2,3
even_mid_node = find_middle_element(even_ll)
odd_mid_node = find_middle_element(odd_ll)
print(even_mid_node) #3
print(odd_mid_node) #2
