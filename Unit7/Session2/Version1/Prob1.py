#Unit 7
#session 2
#ver 1
#prob 1

# sliding window with recursion
# check the current char and the last curr char
# shrink the list 
def is_nested(paren_s):
  if len(paren_s) == 0:
      return True
#check if lenght of string is zero


  if paren_s[0] == '(' and paren_s[-1] == ')':

#checks if its an opening paranthesis and if last character is a closing paranthesis

      return is_nested(paren_s[1:-1])
  else:
      return False


print(is_nested("((())")) #False
print(is_nested("(())")) #True
print(is_nested('(')) #False