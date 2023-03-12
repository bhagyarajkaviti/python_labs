#Write a function with the name get_speed_status that takes the speed (S) as an argument.
#- If the speed is less than 60, it should return "Normal".
#- If the speed is greater than or equal to 60 and less than 80, it should return "Warning".
#- If the speed is greater than or equal to 80, it should return "Over Speed".
def get_speed_status(speed):
    # Complete this function
    if speed < 60:
        status = "Normal"
    elif speed >= 60 and speed < 80:
        status = "Warning"
    else:
        status = "Over Speed"
    
    return status
speed = int(input())
# Call the get_speed_status function
print(get_speed_status(speed))