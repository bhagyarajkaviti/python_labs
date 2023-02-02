#write a program that reads a temperature and checks if the given temperaature is between 15 and 40.
    #Print can go for a walk if the given temperature is between 15 and 40, otherwise print Cannot go for a walk.
temperature = int(input())

if (temperature > 15 and temperature < 40):
    print("Can go for a walk")
else:
    print("Cannot go for a walk")