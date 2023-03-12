#Write a function with the name get_weather_report that takes the temperature as an argument.
#- If the temperature is less than 22, it should return "Cold".
#- If the temperature is greater than or equal to 22 and less than 35, it should return "Warm".
#- If the temperature is greater than or equal to 35, it should return "Hot".
def get_weather_report(temperature):
    # Complete this function
    if temperature < 22:
        status = "Cold"
    elif temperature >= 22 and temperature < 35:
        status = "Warm"
    else:
        status = "Hot"
        
    return status
        
temperature = int(input())
# Call the get_weather_report function
print(get_weather_report(temperature))