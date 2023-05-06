#You are given the arrival and departure times of some trains in 24- hour format. Your task is to determine the minimum number of platforms needed at a railway station to accommodate all trains arriving and departing (i.e. ensuring that no two trains overlap at a single platform and no train is left waiting).
#All trains arrive and depart on the same day, with distinct arrival and departure times. To prevent conflicts, separate platforms are needed for trains whose arrival overlaps with the departure of another train on the same platform.
#Write a program that reads the arrival and departure times of the trains in 24-hour format and prints the minimum number of platforms needed at a railway station to accommodate all trains.
#Input
#The first line of input contains space-separated integers representing the arrival times of the trains in 24-hour format.
#The second line of input contains space-separated integers representing the departure times of the trains in 24-hour format.


arrival = list(map(int, input().split()))
arrival.sort()
departure = list(map(int, input().split()))
departure.sort()

i= 1
j = 0
min_pfs = 1
max_pfs = 1
while i < len(arrival) and j < len(arrival):
    inn = arrival[i]
    out = departure[j]
    if arrival[i] <= departure[j]:
        min_pfs += 1
        i += 1
    else:
        min_pfs -= 1
        j += 1
    if min_pfs > max_pfs:
        max_pfs = min_pfs
print(max_pfs)