#unit 3
#session 2
#version 3
#prob 3

#Edge Cases
#pattern = None, s = None, output = True
#pattern = None, s = "ageoa agoa", output = False
#pattern = "aaaa", s = None, output = False
#pattern = "", s = "", output = True
#pattern = "", s = "dot toa jgaol", output = False
#pattern = "abba", s = "", output = False
#pattern = "abba", s = "dog cat cat dog", output= True
#pattern = "aaaa", s = dog dog dog dog", output = True
#pattern = "abba", s= 'dog cat dog', output = False


#High Level Plan
#Hash map approach 
  #create a hash map {'a': 'word of the str s'}
  #Split the s string to list
  #iterate ove the list and fill up the map
  #use a for loop for the len of the list
    #compare the curr ele of the list is equal to the value of the curr key in the map

#Low Level Plan
#split the s str into a list
#create a hash map {'the char in the pattern str': "word of the str s"}
#iterate for the len of the list
  #curr ele of the list != the value of the curr key in the map
    #return False 

def wordPattern(pattern, s):
  if not pattern and not s:
    return True
  if not pattern and s:
    return False
  if pattern and not s:
    return False
  
  s_lst = s.split()
  if len(pattern) != len(s_lst):
    return False
    
  pattern_match = {}
  #filling up the pattern_match map
  for i in range(len(s_lst)):
    pattern_match[pattern[i]] = s_lst[i]

  for i in range(len(pattern)):
    if pattern_match[pattern[i]] != s_lst[i]:
      return False
      
  return True

pattern = None
s = None
print(wordPattern(pattern, s)) #True

pattern2 = None
s2 = "dog cat" 
print(wordPattern(pattern2, s2)) #False

pattern3 = "abba"
s3 = None
print(wordPattern(pattern3, s3)) #False

pattern4 = ""
s4 = ""
print(wordPattern(pattern4, s4)) #True

pattern5 = ""
s5 = "dog cat"
print(wordPattern(pattern5, s5)) #False

pattern6 = "abba"
s6 = ""
print(wordPattern(pattern6, s6)) #False

pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s)) #True
s2 = "dog cat cat fish"
print(wordPattern(pattern, s2)) #False

pattern2 = "aaaa"
s3 = "dog cat dog cat"
print(wordPattern(pattern2, s3)) #False
s4 = "dog dog dog dog"
print(wordPattern(pattern2, s4)) #True