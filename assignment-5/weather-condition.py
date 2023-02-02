#Write a program to display a customized message based on temperature T.
#Print Freezing weather if T<0                      #Print Very Cold weather if 0 <= T < 10
#Print Cold weather if 10 <= T < 20                 #Print Normal if 20 <= T < 30
#Print Hot if 30 <= T < 40                          #Print Very Hot if T >= 40
T = float(input())

if T < 0:
    print("Freezing weather")
elif 0 <= T < 10:
    print("Very Cold weather")
elif 10 <= T < 20:
    print("Cold weather")
elif 20 <= T < 30:
    print("Normal")
elif 30 <= T < 40:
    print("Hot")
elif T >= 40:
    print("Very Hot")