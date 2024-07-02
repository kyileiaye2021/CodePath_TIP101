#unit 4
#session 2
#ver 3
#prob 5

# Two Pointer Approach
# create a pointer to store the index of start of the sliding window
# create a var to store the neg count
# iterate over the list
#   check the curr ele is neg
#     increment neg count
#   if curr index reaches the end of the sliding window  (i - start + 1 == k)
#     check the start index var is neg
#       decrement the neg count by 1
#      increment the start by 1

def count_negatives(nums, k):
  count_lst = []
  neg_count = 0
  start = 0
  for i in range(len(nums)):
    if nums[i] < 0:
      neg_count += 1

    if i - start + 1 == k:
      count_lst.append(neg_count)
      if nums[start] < 0:
        neg_count -= 1
      start += 1

  return count_lst

lst = [-1, 2, -2, 3, 5, -7, -5]
print(count_negatives(lst, 3))

