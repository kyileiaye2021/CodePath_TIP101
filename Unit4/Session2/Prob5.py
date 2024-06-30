#unit 4
#session 2
#ver 1
#prob 5

# Low Level Planning
# * Sliding Window Technique
# * iterate over the str until the three char from the last char
#   * define the window for each iteration
#   * check there are duplicates in the window and return num of count 
#   * return that num

def check_duplicate(window):

  frequency = {}
  for ele in window:
    if ele not in frequency:
      frequency[ele] = 1
    else:
      return 0
  return 1

def count_good_substrings(s):
  good_str_count = 0
  for i in range(0, len(s) - 2):
    window = s[i : i + 3] #sliding window
    curr_count = check_duplicate(window)
    good_str_count += curr_count 
  return good_str_count

s1 = "xyzzaz"
s2 = "xyzxyz"
print(count_good_substrings(s1))
print(count_good_substrings(s2))