#1. _convert_cel_to_far()_ which takes one float parameter representing degrees Celsius and returns
#  a float representing the same temperature in degrees Fahrenheit using the following formula:

#F = C \* 9/5 + 32

#2. _convert_far_to_cel()_ which take one float parameter representing degrees Fahrenheit and returns 
# a float representing the same temperature in degrees Celsius using the following formula:
 
# C = (F - 32) \* 5/9_

#The script should first prompt the user to enter a temperature in degrees Fahrenheit and then display 
# the temperature converted to Celsius. Then prompt the user to enter a temperature in degrees Celsius 
# and display the temperature converted to Fahrenheit. All converted temperatures should be rounded to 
# 2 decimal places.


def temperature(dec):
    
    a = (dec * 9/5) + 32
    print(f"{dec} degrees C = {a} degrees F")

temperature(float(input("Enter a temperature C: ")))

def temperature(deff):
    
    b = (deff - 32) * 5/9
    print(f"{deff} degrees F = {b} degrees C")

temperature(float(input("Enter a temperature F: ")))