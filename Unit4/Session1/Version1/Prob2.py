#unit 4
#session 1
#ver 1
#prob 2

#create two pointers 
# make for loop until a pass b
#   swap two pointers var 
#    move a to right by 1
#    move b to left by 1

def reverse_list(lst):
  a = 0 
  b = len(lst) - 1
  while a < b:
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp
    a += 1
    b -= 1
  return lst
lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))

#Time complexity - O(n) 
#Space complexity - O(1)
