#What time is it?

#Create a func with a integer parameter that return a string based on the specific conditions

def what_time_is_it(hour):
  if hour == 2:
    return "taco time 🌮"
  elif hour == 12:
    return "peanut butter and jelly time 🧀🫓"
  else:
    return "nap time 😴"

time = what_time_is_it(15)
print(time)
