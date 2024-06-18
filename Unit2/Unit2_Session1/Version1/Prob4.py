#unit 2
#session 1
#ver 1
#problem 4

#create two vars to keep track of total_keys and total_values
#iterate over the dict
#accumulate the two vars in each iteration
#compare those two vars aftter iteration
#return the str based on the conditions

def keys_v_values(dictionary):
  total_keys = 0
  total_values = 0

  for key, value in dictionary.items():
    total_keys += key
    total_values += value

  if total_keys > total_values:
    return "keys"
  elif total_values > total_keys:
    return "values"
  else:
    return "balanced"

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)