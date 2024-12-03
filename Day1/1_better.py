from collections import Counter

lines = open('input.txt').read().split('\n')
left, right = [], []
count = Counter()
for line in lines:
    a,b = map(int, line.split())
    left.append(a)
    right.append(b)
    count[b] += 1
left.sort()
right.sort()
distance = 0

for x,y in zip(left, right):
    distance += abs(x-y)

print(distance)

similarity = 0

for x in left:
    similarity += x * count.get(x, 0)
print(similarity)