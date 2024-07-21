#unit 7
#session 2
#ver 3
#prob 4

# Find frequencies of ele in less than O(n)

# High Level plan
# create a hash map
# iterate thru the list until the length of the list
#    check if the ele is in the hash map
#      continue to another ele
#    find the first occurence of the ele in binary search
#    find the last occurence of the ele in binary search
#    count it (last - first + 1)
#    move i to last + 1 index to check for another ele


def find_first(lst, target):
  left, right = 0, len(lst) - 1
  while left <= right:
    mid = (left + right) // 2
    if lst[mid] >= target:
      right = mid - 1

    else:
      left = mid + 1

  return left

def find_last(lst, target):
  left, right = 0, len(lst) - 1
  while left <= right:
    mid = (left + right) // 2
    if lst[mid] <= target:
      left = mid + 1
    else:
      right = mid - 1
  return right

def find_frequencies(lst):
  frequencies = {}
  lst_len = len(lst)
  i = 0
  while i < lst_len:

    first = find_first(lst, lst[i])
    last = find_last(lst, lst[i])
    count = last - first + 1
    frequencies[lst[i]] = count

    i = last + 1

  return frequencies

lst = [2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9]
print(find_frequencies(lst))
# Expected Output: {2: 3, 4: 3, 5: 2, 6: 1, 8: 2, 9: 1}