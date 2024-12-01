import numpy as np

# Splits input.txt into 2 arrays for sorting and comparison
inputFile = open("input.txt", "r");
locIDs = inputFile.readlines()

list1 = []
list2 = []

for pair in locIDs:
    nums = pair.split()
    list1.append(int(nums[0]))
    list2.append(int(nums[1]))

similarityScore = 0

for i in range(0, len(list1)):
    similarityScore += (list2.count(list1[i]) * list1[i])

print(similarityScore)