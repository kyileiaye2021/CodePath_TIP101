#unit 1
#session 2
#ver 2
#problem 7

#create a func with a list as a param
#create a new list to store only odd nums
#use % operator to know the ele is odd num (if ele isn't divisible by 2)
#put ele in the new list and return 

def get_odds(nums):
  new_list = []
  for ele in nums:
    if ele % 2 != 0:
      new_list.append(ele)

  return new_list

nums = [2,5,1,8,6,5]
odd_nums = get_odds(nums)
print(odd_nums)