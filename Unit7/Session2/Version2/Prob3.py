#unit 7
#session 2
#ver 2
#prob 3

# base case (when the left > right)
# recursive case

def count_zeros_recursive(lst, left, right):
  # base case:
  if len(lst) == 0:
    return 0

  if left > right and right < len(lst):
    return (right + 1)

  # recursive case:
  mid = (left + right) // 2

  if lst[mid] > 0:
    return count_zeros_recursive(lst, left, mid - 1)

  else:
    return count_zeros_recursive(lst, mid + 1, right)


def count_zeros(lst):
  left = 0
  right = len(lst) - 1
  return count_zeros_recursive(lst, left, right)

lst = [0,0,0,0,1,1]
print(count_zeros(lst)) #4

lst2 = [0,0,1,1] 
print(count_zeros(lst2)) #2

lst3 = [0]
print(count_zeros(lst3)) #1

lst4 = []
print(count_zeros(lst4)) #0

#Time complexity : O(logn)
#Space complexity: O(log(n))