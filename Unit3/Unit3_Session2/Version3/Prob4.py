#unit 3
#session 2
#version 3
#prob 4

#Edge Cases
#input = "", output = 0
#input = None, output = 0
#input = "0", output = 0
#input = "1", output = 0
#input = "1111", output = 0

#High Level Plan
#* Brute Force
  #iterate over the string and find the substring starting from the current char| check the substring met the conditions 
#* Two poiner approach
  #starting and end of the substr are maintained by left and right pointers
  #create counter to keep track of the num of substr that meets the conditions
  #keep track of curr length 
  #in the iteratioin of the str, if the curr char change from 0 to 1, reset the current length to 0 |otherwise, update the current length
  #store each length of the substring group, compare and get the smallest length of the group and add it to the counter


#Low Level plan
# create two pointers left and right point to index 0
# careate a curr length var to store the curr length of the group 
# create a list to store the length of each group of substring
# iterate over the string 
  #check if curr char change from 0 to 1
    #append the curr length to group length list
    #increment left by curr length
    #reset current length to 1
  #if it's not
    #increment the curr length by 1
  #increment right by 1

# create a counter initialzed to 0
#iterate over the group length list 
  #check curr length < prev length
    #counter += curr length
    
def binary_substrings_count(s):
  if not s:
    return 0
  r = 1
  curr_length = 1
  group_length_list = []

  while r < len(s):
    if s[r] != s[r-1]:
      group_length_list.append(curr_length)
      curr_length = 1

    else:
      curr_length += 1

    r += 1
  group_length_list.append(curr_length)

  counter = 0

  for i in range(1,len(group_length_list)):
    counter += min(group_length_list[i], group_length_list[i-1])

  return counter


s = "00110011"
print(binary_substrings_count(s)) #6

s2 = "10101"
print(binary_substrings_count(s2)) #4

s3 = "1111"
print(binary_substrings_count(s3)) #0

s4 = ""
print(binary_substrings_count(s4)) #0

s5 = None
print(binary_substrings_count(s5)) #0

s6 = "0"
print(binary_substrings_count(s6)) #0

s7 = "1"
print(binary_substrings_count(s7)) #0