#unit 2
#Session 2
#Ver 1
#Prob 7

#create a dict {item, occurence}
#iterate over the list
#put the key-val pair in the dict

#calculate the number of pairs (len(lst) / 2)
#create the var to keep track of the count of pairs
#iterate over the dict
#in each iteration, check the val is divisible by 2 and update the count
#if not, return False
#if every pair works, check the count == num of pairs
#return True if everything works

def divideList(nums):
  dict = {}
  for ele in nums:
    if ele in dict:
      dict[ele] += 1
    else:
      dict[ele] = 1

  possible_pair_num = len(nums) / 2
  pair_count = 0
  for key in dict:
    if dict[key] % 2 == 0:
      pair_count += dict[key] / 2
    else:
      return False

  if pair_count == possible_pair_num:
    return True


nums = [3,2,3,2,2,2]
print(divideList(nums))
nums = [1,2,3,4]
print(divideList(nums))