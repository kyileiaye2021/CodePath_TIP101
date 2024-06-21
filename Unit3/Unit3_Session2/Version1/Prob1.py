#unit 3
#session 2
#ver 1
#prob 1

#create a var to keep track of total sum
#iterate thru the list
  #convert the curr ele to the int type
  #update total sum
#return the total sum

def sum_of_number_strings(nums):
  total_sum = 0
  for n in nums:
    total_sum += int(n)
  return total_sum

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)