#unit 3
#session 2
#version 3
#prob 1

#Edge cases
#1. input = "", output = None
#2. input = None, output = None
#3. input = "Hel", ouput = "Hl"

#High level plan
#Iterative Approach
#create a new str
#check each char in orig str, remove it if it's a vowel

#Low level plan
#creat a vowel str (aeiouAEIOU)
#create a var to store 
#iterate over the orig str
    #check if the curr char in the str
    #if it's not,
        #concatenate the curr char to the new str
#return the new str

def remove_vowels(s):
  vowel = 'aeiouAEIOU'
  new_str = ''
  if not s:
    return None
    
  for char in s:
    if char not in vowel:
      new_str += char
  return new_str


new_string1 = remove_vowels(None)
print(new_string1)
new_string2 = remove_vowels("")
print(new_string2)
s = "Hello World"
new_string3 = remove_vowels(s)
print(new_string3)

