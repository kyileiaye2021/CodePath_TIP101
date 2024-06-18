#Unit 1
#Session 1 Problem Set Version 2
#Problem 4

#a func with an int type param
# prints out based on the conditions

def sleep_assessment(hours):
  if hours < 8:
    print("Oof, go back to bed!")
  elif hours >= 8 or hours <= 10:
    print("You got a good night's rest!")
  else:
    print("You're a sleep prodigy!")

sleep_assessment(10)
sleep_assessment(4)
sleep_assessment(12)
sleep_assessment(9)

