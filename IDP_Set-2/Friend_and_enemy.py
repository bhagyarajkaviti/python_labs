#A group of F friends visited a haunted house. Each member was wearing a shirt with a number on it ranging from 1 to F. As they entered the haunted house, one of them was kidnapped and an enemy replaced him.
#Rather than wearing the same shirt number as the kidnapped one, the enemy wore a shirt with the same number as another person among the remaining people.
#Write a program that reads the F space-separated numbers and prints the numbers on the shirt of the enemy and the person who was kidnapped.
#Input
#The input will be a single line containing space-separated integers representing all the people who are currently in the house, from 1 to F.

with_enemy = list(map(int, input().split()))
l = len(with_enemy)

output = []
for i in with_enemy:
    if with_enemy.count(i) == 2:
        common = i
        output.append(i)
        break
with_friends = set(range(1,l+1))

missed = with_friends.difference(with_enemy)
output.extend(missed)
print(*output)