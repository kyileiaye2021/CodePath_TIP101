#unit 2
#session 1
#ver 3
#prob 4

#create a var to count the num of present in the dict
#iterate over the dict
#check the value is present , accumulate the count var
#calculate the percentage 
#return that percentage

def attendance_rate(attendance_list):
  present_count = 0
  for attendent in attendance_list:
    if attendance_list[attendent] == "Present":
      present_count += 1

  percentage = (100 / len(attendance_list)) * present_count
  return percentage

attendance_list = {
  "Bluey": "Present", 
  "Bingo": "Absent", 
  "Snickers": "Present", 
  "Winton": "Absent"
}

print(attendance_rate(attendance_list))