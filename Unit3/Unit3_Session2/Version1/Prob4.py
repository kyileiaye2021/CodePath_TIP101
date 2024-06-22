#unit 3
#session 2
#ver 1
#prob 4

def longest_uniform_substring(s):
  count = 1
  longest = 1
  for i in range(1, len(s)):
    if s[i] == s[i-1]:
      count +=1 
      longest = max(longest, count)
    else:
      count = 1
  return longest

s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)