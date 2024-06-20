#unit 3
#session 1
#ver 2
#prob 4

'''
Key Takeaways
We can use slicing method to reverse the list 
Instead of using for loop, we can use .join() to concatenate the str
'''
#splittin up the input str
#if the size of the list is 1
  #return the orig str
#create a new str
#iterate over the list in reverse
  #concatenate the curr ele to the new str
#return the new str

def reverse_sentence(sentence):
  word_list = sentence.split()
  reversed_word_list = word_list[::-1]
  reversed_sentence = " ".join(reversed_word_list)
  return reversed_sentence

sentence = 'I solemnly swear I am up to no good'
print(reverse_sentence(sentence))