#Classify Age() func

#create a func with an int type parameter and return a string

def classify_age(age):
  if age < 18:
    return "child"
  else:
    return "adult"

output = classify_age(18)
print(output)