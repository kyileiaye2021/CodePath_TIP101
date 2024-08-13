#unit 10
#session 1
#ver 3
#prob 3

'''Happy Case'''
#input - 1->2->3->4->5->6->7-> 8 -> 9 -> 10 -> 11 -> 12 -> 13
#head - 1, m = 2, n = 3
# output - 1->2->6->7->11->12

'''Edge Case'''
# input - None
# head - None, m = 2, n = 3
# output - None

# input - 1->2
# head - 1, m = 2, n = 3
# output - 1->2

# Initialize curr pointer to 0
# iterate over the ll until curr is none
# traverse the nodes for m nodes
#   move the current pointer `m` steps forward
# create a temp node to the next node of curr kept node 
#   move temp pointer n steps, skip the n nodes
# point the curr pointer to the next node of temp node
# repeat the process
# return the head

'''
Time complexity - O(n)
Space complexity - O(1)
'''
class Node:
  def __init__(self, val=0, next=None):
      self.value = val
      self.next = next

def delete_nodes(head, m, n):
  curr = head

  while curr:

    for _ in range(m-1):
      if not curr:
        return head
      curr = curr.next

    temp = curr.next

    if not temp:
      return head

    for _ in range(n):
      if not temp:
        break
      temp = temp.next

    curr.next = temp
    curr = curr.next

  return head

def print_ll(head):
  while head.next:
    print(f'{head.value}->',end='')
    head = head.next
  print(head.value)

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12))))))))))))
print_ll(delete_nodes(head, 2, 3))

head = Node(1, Node(2))
print_ll(delete_nodes(head, 2,3))
