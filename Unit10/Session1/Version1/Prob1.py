#unit 1
#session 1
#ver 1
#prob 1

# initialize an empty stack
# go over the string and 
# check if each char is open paranthesis:
#   put the cur char in the stack
# if it is close paren, 
# check the last element is not equal to the val of close paren
#    return False

def is_valid(s):
  if len(s) == 0: 
    return True
  stack = []
  Bracket_type = {')':'(', '}':'{', ']':'['}


  for char in s:
    if char in Bracket_type.values(): # if the curr char is open paren
      stack.append(char)
    else: # if curr char is close paren
      last_ele = stack[-1] 
      if last_ele == Bracket_type[char]: #check the last ele in stack is the open paren of curr closed paren
        stack.pop()
      else:
        return False

  return len(stack) == 0


s = "()"#true
print(is_valid(s))
s = "()[]{}"#true
print(is_valid(s))
s = "(())"#true
print(is_valid(s))
s = "(]"#false
print(is_valid(s))

# Time complexity - O(n)
# Space complexity - O(n)