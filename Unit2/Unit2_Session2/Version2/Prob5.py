#unit 2
#session 2
#ver 2
#prob 5

#create a dict {val, occurence}
#iterate over the list and fill the dict
#create a list to store the keys that have the most frequent mode
#create a var to store the largest mode
#iterate over the dict
#update the largest mode
#update the list

def find_mode(lst):
  occurence_dict = {}
  largest_mode = 0
  largest_mode_key = None

  for i in lst:
    if i not in occurence_dict:
      occurence_dict[i] = 1
    else:
      occurence_dict[i] += 1

    #find the largest mode in the dict
    if occurence_dict[i] > largest_mode:
      largest_mode = occurence_dict[i]
      largest_mode_key = i #find the key that has largest mode

  return largest_mode_key

lst = [1,2,3,2,3,3,4,4,4,4]
mode = find_mode(lst)
print(mode)