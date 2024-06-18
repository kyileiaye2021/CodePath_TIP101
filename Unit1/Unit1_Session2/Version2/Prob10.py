#unit 1
#session 2
#ver 2
#problem 10

#create a func with a list as a param
#create a var called count to count the 0s in the list
#create a neew list
#iterate over the list and check the current ele is 0 or not
#if it's not, append it to the new list
#if it's, increment count var by 1
#append 0 to the list for that num of count var


#we can use count built-in func instead of manually counting the num of zeros

def move_zeroes(nums):
  count_zero = 0
  new_list = []
  for ele in nums:
    if ele != 0:
      new_list.append(ele)

    else:
      count_zero += 1

  for _ in range(count_zero):
    new_list.append(0)

  return new_list


nums = [1,0,2,3,0,0,4]
new_nums = move_zeroes(nums)
print(new_nums)