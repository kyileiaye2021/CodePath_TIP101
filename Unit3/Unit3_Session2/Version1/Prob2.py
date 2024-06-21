#unit 3
#session 2
#ver 1
#prob 2

#create a var to keep track of the index that points to the unique ele 
#iterate thru the orig list
  #if curr ele != prev ele:
    #update the ele the unique ele index var is currently pointing to
    #update the unique ele index var by incrementing by 1
#return the orig list starting from index 0 to the unique ele index list

def remove_duplicates(nums):
  unique_ele_index = 1
  i = 1
  while i < len(nums):
    if nums[i] != nums[i-1]:
      nums[unique_ele_index] = nums[i]
      unique_ele_index += 1
    
    i += 1
  return nums[:unique_ele_index]

nums = [1,1,1,2,3,4,4,5,6,6]
remove_duplicates(nums)
