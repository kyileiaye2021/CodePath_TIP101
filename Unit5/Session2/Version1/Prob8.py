#unit 5
#session 2
#ver 1
#prob 8

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def list_to_linked_list(lst):
  linked_lst_str = ""
  head = Node(lst[len(lst) - 1])
  for i in range(len(lst) - 2, -1, -1):
    head = Node(lst[i], head)

  while head:
    if head.next:
      linked_lst_str += head.value + ' -> '
    else:
      linked_lst_str += head.value
    head = head.next
  return linked_lst_str

normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)
print(linked_list) # Only prints the head element!