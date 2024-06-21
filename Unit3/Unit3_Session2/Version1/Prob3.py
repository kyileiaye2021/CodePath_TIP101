#unit 3
#session 2
#ver 1
#prob 3
'''
Key Takeaways
Strings are immutable so the chars of the string cannot be assigned or updated. So, convert a str to char list before swapping.
'''
#create a temp pointer that firstly is last index
#iterate through the string s until the curr char passes the temp pointer
  #if the curr char is alphabetic 
    #if the char that temp pointer points to is also alphabetic
      #swap the two elements
    #decrement the temp pointer by 1
  #increment the curr index by 1
#return the string s

def reverse_only_letters(s):
  char_lst = list(s)
  right = len(char_lst) - 1
  i = 0
  
  while i < right:
    
    if char_lst[i].isalpha():
      
      if char_lst[right].isalpha():
        temp = char_lst[i]
        char_lst[i] = char_lst[right]
        char_lst[right] = temp
        
      right -= 1
    i += 1
    
  s = ''.join(char_lst)
  return s
  
s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)
