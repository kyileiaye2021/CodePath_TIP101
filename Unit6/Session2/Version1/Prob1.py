#unit 6
#session 2
#ver 1
#prob 1

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def is_circular(head):

  fast, slow = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
      return True

  return False

num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num1
# num1 -> num2 -> num3 -> num1
print(is_circular(num1))

var1 = Node(1)
var2 = Node(2)
var3 = Node(3)
var1.next = var2
var2.next = var3
# var1 -> var2 -> var3
print(is_circular(var1))