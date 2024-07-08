#unit 5
#session 2
#ver 3
#prob 2

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

red = Node('red')
yellow = Node('yellow')
blue = Node('blue')
red.next = yellow
yellow.next = blue

# Current list: red -> yellow -> blue
# Desired list: red -> orange -> yellow -> green -> blue

orange = Node('orange')
green = Node('green')
orange.next = yellow
red.next = orange
green.next = blue
yellow.next = green

curr_head = red
while curr_head:
  if curr_head.next:
    print(f'{curr_head.value} -> ', end='')
  else:
    print(curr_head.value)
  curr_head = curr_head.next
