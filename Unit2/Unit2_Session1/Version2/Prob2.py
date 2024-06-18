#unit 2
#session 1
#ver2
#prob 2

#create a dict
#iterate over the list using range func
#assign the current item of the list and the index in the dict
#return dict

def student_directory(student_names):
  student_dict = {}
  for i in range(1, len(student_names) + 1):
    student_dict[student_names[i-1]] = i

  return student_dict

student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]

print(student_directory(student_names))