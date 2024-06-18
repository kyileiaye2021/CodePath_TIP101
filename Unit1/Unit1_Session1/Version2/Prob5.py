#Unit1
#Session 1 Ver 2
#Problem 5

#Calculate Tips
#a func with two param: float type bill and string type service quality
#return a float value based on the service quality

def calculate_tip(bill, service_quality):
  match service_quality:
    case "poor":
      return bill * 0.1

    case "average":
      return bill * 0.15

    case "excellent":
      return bill * 0.2

    case _:
      return None

tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)
