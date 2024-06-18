#unit 2
#session 1
#ver 1
#Problem 6

def calculate_gpa(report_card):
  #create a grade dict
  grades = { 
  "A": 4,
  "B": 3,
  "C": 2,
  "D" :1,
  "F": 0
  }

  total = 0
  #check the values in the iteration 
  #and accumulate the total variable
  for values in report_card.values():
    if values == "A":
      total += grades["A"]
    elif values == "B":
      total += grades["B"]
    elif  values == "C":
      total += grades["C"]
    elif values == "D":
      total += grades["D"]
    elif values == "F":
      total += grades["F"]
  final_grade = float(total/len(report_card))
  return final_grade


report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))
