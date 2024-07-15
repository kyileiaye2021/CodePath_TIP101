#unit 6
#session 2
#ver 2
#prob 6

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def print_ll(head):
  curr_head = head
  while curr_head.next != head:
    if curr_head.next:
      print(f"{curr_head.value} -> ", end='')
    curr_head = curr_head.next
  print(f"{curr_head.value} -> {curr_head.next.value}")


def delete_node(head, val):
  if not head:
    return None

  if head == head.next:
    return None

  prev = None
  current = head
  while True:
    if current.value == val:

      if current == head:
        #need to find the tail of circular linked list
        tail = head
        while tail.next != head:
          tail = tail.next

        head = head.next #reset the head (cause head is now removed)
        tail.next = head #make the ll circular

      else:
        prev.next = current.next

      return head    
    prev = current
    current = current.next

    ## Since it's circular, stop if we have gone through the list once
    if current == head:
      break

# num1 -> num2 -> num3 -> num1
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num1
print_ll(delete_node(num1, 1)) # 2 -> 3 -> 2

# num1 -> num2 -> num3 -> num1
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num1
print_ll(delete_node(num1, 2)) # 1 -> 3 -> 1





