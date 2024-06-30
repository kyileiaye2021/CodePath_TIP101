#unit 4
#session 1
#ver 1
#prob 5

'''
Look at the range func length in detail
'''
# Two pointer approach (sliding window)
# create a list to store avg values
# iterate over the nums from index 0 to last index - 5
  # slide the window for the range of k
  # iterate over the window
    # get the average of the curr window
    # put it in the list
# return the list

def get_average(window, k):
  total = 0
  for ele in window:
    total += ele
  return (total / k)

def find_averages_of_subarrays(k, nums):
  avg_lst = []
  for i in range(len(nums) - k + 1):
    window = nums[i:i+k]
    avg = get_average(window, k)
    avg_lst.append(avg)
  return avg_lst

nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
avg_lst = find_averages_of_subarrays(5, nums)
print(avg_lst)
