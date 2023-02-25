#You are given the temperature T of an object in one of Celsius, Fahrenheit, and Kelvin scales.
#Write a program to print T in all scales viz Celsius, Fahrenheit, and Kelvin.
#Formula to convert from Fahrenheit F to Celsius C is 
#           C = (F - 32) * 5 /9
#Formula to convert from Kelvin K to Celsius C is
#           C = K - 273
#Here "C", "F", "K" represent that the temperature scale is in Celsius, Fahrenheit and Kelvin scales respectively.
#The input contains the temperature (a number) and the unit of the temperature scale (C, F, K) without any space.
#The output contains temperature in Celsius, Fahrenheit and Kelvin scales in each line in the format similar to input and the value of the temperature is rounded to 2 decimal places.

temperature_in_degrees = input()
unit = temperature_in_degrees[len(temperature_in_degrees) - 1]

temperature = float(temperature_in_degrees[:len(temperature_in_degrees) - 1])
temperature = round(temperature,2)

if unit == "C":  # if given input temperature is in Celsius
    print(str(temperature) + unit)
    
    F = ((temperature * 9)/5) + 32
    print(str(F) + "F")
    
    K = temperature + 273
    print(str(K) + "K")
elif unit == "F":   # If the given input temperature is in Fahrenheit
    C = (temperature - 32) * 5 / 9
    C = round(C,2)
    print(str(C) + "C")
    
    print(str(temperature) + unit)
    
    K = C + 273
    K = round(K,2)
    print(str(K) + "K")
elif unit == "K":   # If the given input temperature is in Kelvin
    C = temperature - 273
    C = round(C,2)
    print(str(C) + "C")
    
    F = ((C * 9)/5) + 32
    F = round(F,2)
    print(str(F) + "F")
    
    print(str(temperature) + unit)
    