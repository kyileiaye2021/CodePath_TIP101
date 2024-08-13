#unit 10
#session 2
#ver 2
# prob 1

'''happy case'''
# Input: current_state = "++++"
# Output: ["--++","+--+","++--"]

'''Edge case'''
# Input: current_state = "----"
# Output: []

# Input: current_state = "+"
# Output: []

# iterative approach
# create a list to store the str
# iterate over the str
#   check if the curr char and the next char is + 
#     change those to -- and append it to the list
# return list

def generate_possible_next_moves(current_state):
  res = []

  for i in range(len(current_state) - 1):
    if current_state[i] == '+' and current_state[i + 1] == '+':
      new_state = current_state[ : i] + '--' + current_state[i+2 : ]
      res.append(new_state)
      
  return res
  
input = "++++"
print(generate_possible_next_moves(input)) # ["--++","+--+","++--"]

input ="----"
print(generate_possible_next_moves(input)) # []

input = '+'
print(generate_possible_next_moves(input)) # []

input =  "++--"
print(generate_possible_next_moves(input)) # [----]