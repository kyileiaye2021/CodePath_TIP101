#unit 4
#session 2
#ver 3
#prob 6

# Two pointer approach with sliding window
# * create a var to store the max total count of vowels within the substring
# * create a var to store the curr count of vowels first initialized to 0
# * let start of the sliding window be 0
# * iterate over the str s
#   * check the curr ele is vowel
#     * increment the curr vowel count
#   * if the curr index reaches the end of the sliding window  (i - start + 1 == k)
#     * max_vowel_count = max(max_vowel_count, curr_vowel_count)
#     * if the start index var is vowel
#        * decrement the curr vowel count
#     * start += 1
def max_vowels(s, k):
  vowels = 'aeiouAEIOU'
  max_vowel_count = 0
  curr_count = 0
  start = 0

  for i in range(len(s)):
    if s[i] in vowels:
      curr_count += 1

    if i - start + 1 == k:
      max_vowel_count = max(max_vowel_count, curr_count)
      if s[start] in vowels:
        curr_count -= 1
      start += 1
      
  return max_vowel_count

s = "abciiidef"
print(max_vowels(s, 3))

print(max_vowels(s, 5))