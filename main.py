def binary_substrings_count(s):
  if not s:
    return 0
  l, r = 0, 1
  curr_length = 1
  group_length_list = []

  while r < len(s):
    if s[r] != s[r-1]:
      group_length_list.append(curr_length)
      l += curr_length
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