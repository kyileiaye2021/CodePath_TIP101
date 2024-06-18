#unit 1
#session 2
#ver 2
#problem 9

#create a func with a list
#initialize a var to the first ele of the list
#iterate over the ele in the list from index 1 to n-1
#multiply the var with 10
#add the current value to the var

def list_to_number(digits):
  var = digits[0]
  for i in range(1, len(digits)):
    var *= 10
    var += digits[i]

  return var

digits = [1,0,3]
number = list_to_number(digits)
print(number)