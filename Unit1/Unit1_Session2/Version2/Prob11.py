#unit 1
#session 2
#ver 2
#problem 11

# create a func with a list as a param
# use range func starting from index 0 to the len of the list incremented by 2 in each iteraton
# print out the ele 


def print_odd_indices(nums):
  for i in range(1,len(nums),2):
    print(nums[i])

nums = [3,4,8,1,5,2]
print_odd_indices(nums)