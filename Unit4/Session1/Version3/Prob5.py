#unit 4
#session 1
#ver 3
#prob 5

# Assumption
# String cannot be null or empty
# ch can or cannot be in word
# what if the ch is at the beginning of the word?

# High levl planning
# * Index Mapping Approach
#    * create a dict of ele and index. Then, get the index of ele and swap the ele from index 0 to that index
# * Two pointer approach
#    * create a var to store the index of ch. Iterate over the word from index 0 to ch to swap

# Low level planning
# * Two pointer approach
#    * create a var to store the index of ch
#    * iterate over the str and find the index of ch
#    * create a list 
#    * create left and right pointer
#    * iterate over the list until left passes right
#        * swap the two pointer
#        * shift both pointers inward
#    * return the joined list

def reverse_prefix(word, ch):
  second = 0
  for i, ele in enumerate(word):
    if ele == ch:
      second = i
      break
      
  char_list = list(word)
  first = 0

  while first < second:
    temp = char_list[first]
    char_list[first] = char_list[second]
    char_list[second] = temp
    first += 1
    second -= 1

  return "".join(char_list)
  

word = "abcdefd"
rev_word = reverse_prefix(word, "d")
print(rev_word)

word2 = "helloworld"
rev_word2 = reverse_prefix(word2, "w")
print(rev_word2)

word3 = "xyzxyz"
rev_word3 = reverse_prefix(word3, "a")
print(rev_word3)
