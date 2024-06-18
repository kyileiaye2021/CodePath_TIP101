#unit 2
#session 2
#ver 2
#prob 7


#create a dict {val: occurence}
#num_of_pairs = 0
#iterate over nums list
#if curr item is not in the dict, add the key val pair
#if it's not, update num_of_pairs and the value in the dict

def numIdenticalPairs(nums):
  occurence_dict = {}
  num_of_pairs = 0

  for n in nums:
    if n not in occurence_dict:
      occurence_dict[n] = 1
    else:
      num_of_pairs += occurence_dict[n]
      occurence_dict[n] += 1

  return num_of_pairs

nums = [1,2,3,1,1,3]
ans = numIdenticalPairs(nums)
print(ans)

nums = [1,1,1,1]
ans = numIdenticalPairs(nums)
print(ans)# ans == 6

nums = [1,2,3]
ans = numIdenticalPairs(nums)# ans == 0
print(ans)

