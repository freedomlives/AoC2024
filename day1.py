## Solutions for Advent of Code day 1, 2024

f = open("challenge1data.txt", "r")

line = f.readline()
l1 = []
l2 = []
while(line):
    nums = line.split()
    l1.append(int(nums[0]))

    l2.append(int(nums[1]))

    line = f.readline()

l1.sort()
l2.sort()

distance = 0

for i in range(len(l1)):
    distance += abs(l1[i] - l2[i])
    

print(f'Distance: {distance}')

# Continuing to part 2
similarity = 0
for i in range(len(l1)):
    x = l2.count(l1[i])
    similarity += x*l1[i]

print(f'Similarity: {similarity}')