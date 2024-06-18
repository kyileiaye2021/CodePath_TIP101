#unit 2
#session 2
#ver 1
#prob 3

#1 pointer to the highest_priority_value
#iterate over the dict
#check the curr value is greater than highest priority value
#update the highetst priority value if it's
#iterate over the dict again to find the highest priority value
#remove the ele

#create vars to keep track of the highest priority value
#iterate over the dict and find the highest val

def get_highest_priority_task(tasks):
  highest_priority_val = 1
  perform_task =""
  for task in tasks:
    if tasks[task] > highest_priority_val:
      highest_priority_val = tasks[task]
      perform_task = task

  tasks.pop(perform_task)
  return perform_task


tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)