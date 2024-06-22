#unit 3
#session 2
#ver 2
#prob 2
'''
Key Takeaway
1. for loop doesn't work when removing elements in the iterations of the loops so use while loop
2. if pop() is used to remove the ele, index of the ele to be removed needs to be known
3. if remove() is used, only ele to be removed needs to be known
'''
#create an empty list to store the removed ele
#iterate thru the str
  #find the min value of the list
  #remove that ele
  #append that ele to the list
#return the list

def delete_minimum_elements(nums):
  removed_lst = []
  while nums:
    min_val = min(nums)
    nums.remove(min_val)
    removed_lst.append(min_val)
  return removed_lst

nums = [5,3,2,8,3,1]
removed_lst = delete_minimum_elements(nums)
print(removed_lst)