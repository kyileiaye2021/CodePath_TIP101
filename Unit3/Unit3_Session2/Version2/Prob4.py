#unit 3
#session 2
#ver 2
#prob 4

#create a pointer to keep track the consecutive count
#iterate thru the str
  #if curr ele == prev ele
    #count += 1
  #else:
    #count = 1
#return count
def count_consecutive_characters(str1):
  count = 1
  i = 1
  while i < len(str1):
    if str1[i] == str1[i - 1]:
      count += 1
    else:
      count = 1
    i += 1

  return count

str1 = "aaabbcaaaa"
count = count_consecutive_characters(str1)
print(count)
str2 = "abcde"
count2 = count_consecutive_characters(str2)
print(count2)