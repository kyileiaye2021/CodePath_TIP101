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
    window = s[i : i + 3]
    curr_count = check_duplicate(window)
    good_str_count += curr_count 
  return good_str_count

s1 = "xyzzaz"
s2 = "xyzxyz"
print(count_good_substrings(s1))
print(count_good_substrings(s2))