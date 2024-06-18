#unit1
#session2
#ver2
#problem 1

#create a func with a non-neg floating point param
#create a kevin var
#create a fahrenheit var
#creaate a list and append those two vars
#return the list

def convertTemp(celsius):
  kelvin = celsius + 273.15
  fahrenheit = (celsius * 1.80) + 32.00

  temperature_list = []
  temperature_list.append(kelvin)
  temperature_list.append(fahrenheit)

  return temperature_list

temperatures = convertTemp(23.00)
print(temperatures)