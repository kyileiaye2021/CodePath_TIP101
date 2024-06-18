#unit 1
#session 2
#ver 2
#problem 5

#create a func with a list and a var (n) as params
#sort the list
#use range(n+1) func to iterate over 0 to n
#compare the ele of the list to the current val of the for loop
#if there is a mismatch, return the current val 

def find_missing(nums):
  nums.sort()
  for i in range(len(nums) + 1):
    if nums[i] != i:
      return i


nums = [2,4,1,0,5]
missing_num = find_missing(nums)
print(missing_num)