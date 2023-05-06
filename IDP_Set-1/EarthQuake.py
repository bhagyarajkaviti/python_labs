#Shreya has been given two different earthquake magnitudes A and B and her task is to find how many times earthquake A is more powerful than earthquake B.
#She knows that when the magnitude of an earthquake increases by 1, the amount of energy multiplies by 32. Help Shreya in determining
#the intensity of earthquake A compared to earthquake B.
#Write a program that reads the magnitudes of earthquakes A and B and prints the number of times earthquake A is more powerful than earthquake B.
#Input
#The input will be a single line containing space-separated integers representing the magnitudes of the earthquakes A and B.

a,b = map(int,input().split())
diff = a - b
magnitude = 32**diff
print(magnitude)