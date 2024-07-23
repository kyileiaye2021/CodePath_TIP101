#unit 7
#session 2
#ver 2
#prob 6

'''
The majority element always exist in the array
'''

# Divide and conquer technique with binary search recursive
# divide the array until we get an ele in the array
# check if the left majority is the same as the right majority, return left majority
# if not, count the frequencies with helper func
# if left majority > right majority, return left majority
# else return right majority

def count_frequencies(nums, num, start, end):
  count = 0
  for i in range(start, end + 1):
    if nums[i] == num:
      count += 1

  return count
  
def find_majority(nums, left, right):
  if left == right: #if there is only one ele in the list
    return nums[left]

  mid = (left + right) // 2

  #dividing the array in half
  left_majority = find_majority(nums, left, mid)
  right_majority = find_majority(nums, mid + 1, right)

  # if both left and right majorities are the same, return that number
  if left_majority == right_majority:
    return nums[left]

  #if they are not the same, count frequencies
  left_count = count_frequencies(nums, left_majority, left, right)
  right_count = count_frequencies(nums, right_majority, left, right)

  if left_count > right_count:
    return left_majority
  else:
    return right_majority
  
def majority_element(nums):
  return find_majority(nums, left, right) # for dividing the array recursively and call frequencies


lst = [3,2,3]
print(majority_element(lst))
