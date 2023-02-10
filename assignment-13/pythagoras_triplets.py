#A Pythagorean triplet is a set of three integers a, b, and c such that a²+ b² = c². In the given limit L, find the number of Pythagorean triplets R that can be formed (such that a < b < c).
limit = int(input())

count = 0

for a in range(1, limit + 1):
    for b in range (1, limit + 1):
        for c in range(1, limit + 1):
            if a < b < c:
                if (a ** 2 + b ** 2 == c ** 2):
                    count = count + 1
print(count)