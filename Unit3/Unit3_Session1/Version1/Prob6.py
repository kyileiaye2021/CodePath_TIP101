#unit 3
#session 1
#ver 1
#PRo 6
#to get the min diff, set the diff the max num which in this case is float('inf')
#set both indices of word1 and word2 with the out-of-range indices first to know the indices are updated in for loop
def min_distance(words, word1, word2):

  word1_index = -1
  word2_index = -1
  difference = float('inf')
  for i, word in enumerate(words):
    if word == word1:
      word1_index = i

    elif word == word2:
      word2_index = i

    if word1_index != -1 and word2_index != -1: #if both word1 and word2 are found in the list
      difference = min(difference, abs(word2_index - word1_index))

  return difference


words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)
