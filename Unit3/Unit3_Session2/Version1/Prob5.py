#unit 3
#session 2
#ver 1
#prob 5

#everytime, Ashe is attacked, the duration will be reset to its original val
#Once attacked, he will be poisoned for the duration
#check when it is attacked
  #decremented duration by 1

def find_poisoned_duration(time_series, duration):
  total_poisoned_time = 0
  for i, time in enumerate(time_series):
    if i > 0:
      if time - time_series[i-1] <= duration:
        total_poisoned_time += (time - time_series[i-1]) - 1
      else:
        total_poisoned_time += 3

  return (total_poisoned_time + 3)

time_series = [1,4,9]
damage = find_poisoned_duration(time_series, 3)
print(damage)