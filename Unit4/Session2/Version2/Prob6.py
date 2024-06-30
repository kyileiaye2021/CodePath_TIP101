#unit 4
#session 2
#ver 2
#prob 6

# Two pointer approach
# create a var to count the num of avg greater than threshold
# iterate over the lst from index 0 to index (k-1)
#    slide the window for k size
#    get the avg and compare it to threshold
#    increment the total count by 1 if it's greater
# return the total count

def get_avg(window, k):
  total = 0
  for ele in window:
    total += ele
  return (total / k)
  
def num_of_subarrays(lst, k, threshold):
  total_count = 0
  for i in range(len(lst)-(k-1)):
    window = lst[i:i+k]
    avg = get_avg(window,k)
    if avg >= threshold:
      total_count += 1
  return total_count
  

nums = [2,2,2,2,5,5,5,8]
count = num_of_subarrays(nums, 3, 4)
print(count)
